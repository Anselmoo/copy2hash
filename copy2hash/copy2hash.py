#!/usr/bin/env python
"""copy2hash: Copy or rename any files to hash named files."""

######################################################
#
# copy2hash: - copying or rename files to hash-secured
# files (sha) via the command line
# written by Anselm Hahn (Anselm.Hahn@gmail.com)
#
######################################################

import argparse
import hashlib as hlib
from pathlib import Path
from shutil import copy, SameFileError
import sys

# imported fileformats
import csv
import json
import pickle
import yaml
from dict2xml import dict2xml

try:
    from . import __version__
except ImportError:
    from __init__ import __version__


def log(msg, mode=None):
    """Print messages to display.

    Parameters
    ----------
    msg : str
        Message to print to the terminal.
    mode : int, optional
        If mode is activated, message becomes for:
        1. an error message 
        2. a verbose message 
        3. a warning message
    """
    if mode == 1:
        print(f"[ERROR] {msg}")
    elif mode == 2:
        print(f"[VERBOSE] {msg}")
    elif mode == 3:
        print(f"[WARNING] {msg}")
    else:
        print(msg)


if sys.version < "3.6":
    log("Unsupported Python Version (version < 3.6)!", 1)
    sys.exit(1)


class SHAKeys:
    """Class of available SHA Keys algorithms.
    
    Attributes
    ----------
    sha1 : str
        String for calling secure hash and message digest algorithms [1,2,3].
    sha224 : str
        String for calling secure hash and message digest algorithms [1,2,3].
    sha256 : str 
        String for calling secure hash and message digest algorithms [1,2,3].
    sha384 : str 
        String for calling secure hash and message digest algorithms [1,2,3].
    sha512 : str 
        String for calling secure hash and message digest algorithms [1,2,3].
    blake2b : str
        String for calling secure hash and message digest algorithms [1,4,5].
    blake2s : str
        String for calling secure hash and message digest algorithms [1,4,5].
    md5 : str
        String for calling secure hash and message digest algorithms [1,2].
    sha3_224 : str 
        String for calling secure hash and message digest algorithms [1,4,5].
    sha3_256 : str 
        String for calling secure hash and message digest algorithms [1,4,5].
    sha3_384 : str
        String for calling secure hash and message digest algorithms [1,4,5].
    sha3_512 : str
        String for calling secure hash and message digest algorithms [1,4,5].
    shake_128 : str
        String for calling secure hash and message digest algorithms [1,4,5].
    shake_256 : str
        String for calling secure hash and message digest algorithms [1,4,5].
    
    References
    ----------
    .. [1] https://docs.python.org/3/library/hashlib.html
    .. [2] https://tools.ietf.org/html/rfc1321.html
    .. [3] https://en.wikipedia.org/wiki/NIST_hash_function_competition
    .. [4] https://131002.net/blake/
    .. [5] https://docs.python.org/3/library/hashlib.html#hashlib.blake2b
    
    """

    sha1 = "sha1"
    sha224 = "sha224"
    sha256 = "sha256"
    sha384 = "sha384"
    sha512 = "sha512"
    blake2b = "blake2b"
    blake2s = "blake2s"
    md5 = "md5"
    sha3_224 = "sha3_224"
    sha3_256 = "sha3_256"
    sha3_384 = "sha3_384"
    sha3_512 = "sha3_512"
    shake_128 = "shake_128"
    shake_256 = "shake_256"


class ExportReport:
    """Export the internal copy dictionary.
    
    The ExportReport class is generating the copy- and moving-reports. This class 
    supports the follwing fileformats: 'csv', 'json', 'pkl', 'txt', 'yaml', and 'xml'. 
    It is also possible to export a `pure` ASCII file with an individual 
    file-extension. Furthemore, also a combinition of different fileformats can be 
    chosen.
    
    Parameters
    ----------
    args : dict
            Dictionary of the keywords and values from the parser.
    """

    def __init__(self, args):
        """Initialise the class."""
        self.args = args

    def make_export(self, copy_dict):
        """Make a report of the copying and moving of the files.

        Parameters
        ----------
        copy_dict : dir
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        """
        if self.args["directory"]:
            fname = Path(
                "{}/{}".format(self.args["directory"], self.args["report_name"])
            )
        else:
            fname = Path("./{}".format(self.args["report_name"]))

        for key in self.args["report"]:
            if key == "csv":
                self.write_csv(copy_dict, fname)
            elif key == "json":
                self.write_json(copy_dict, fname)
            elif key == "pkl":
                self.write_pickle(copy_dict, fname)
            elif key == "txt":
                self.write_txt(copy_dict, fname, fxt="txt")
            elif key == "yaml":
                self.write_yaml(copy_dict, fname)
            elif key == "xml":
                self.write_xml(copy_dict, fname)
            else:
                self.write_txt(copy_dict, fname, fxt=key)

    @staticmethod
    def write_csv(copy_dict, fname):
        """Copy-Report in the `csv`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report.
        """
        with open(f"{fname}.csv", "w+") as f:  # Just use 'w' mode in 3.x
            writer = csv.writer(f)
            writer.writerow(copy_dict.keys())
            writer.writerows(zip(*copy_dict.values()))

    @staticmethod
    def write_json(copy_dict, fname):
        """Copy-Report in the `json`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report.
        """
        json_file = json.dumps(copy_dict, indent=4)
        f = open(f"{fname}.json", "w+")
        f.write(json_file)
        f.close()

    @staticmethod
    def write_pickle(copy_dict, fname):
        """Copy-Report in the `pickel`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report.
        """
        f = open(f"{fname}.pkl", "wb+")
        pickle.dump(copy_dict, f)
        f.close()

    @staticmethod
    def write_txt(copy_dict, fname, fxt="txt"):
        """Copy-Report in the `ASCII`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report coming from the parser, by default 'copy_report'. 
        fxt : str
            The individual file extension from the parser.
        """
        with open(f"{fname}.{fxt}", "w+") as f:  # Just use 'w' mode in 3.x
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(copy_dict.keys())
            writer.writerows(zip(*copy_dict.values()))

    @staticmethod
    def write_yaml(copy_dict, fname):
        """Copy-Report in the `yaml`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report.
        """
        yaml_file = yaml.dump(copy_dict, indent=4)
        f = open(f"{fname}.yaml", "w+")
        f.write(yaml_file)
        f.close()

    @staticmethod
    def write_xml(copy_dict, fname):
        """Copy-Report in the `xml`-format.

        Parameters
        ----------
        copy_dict : str
            Internal dictionary will be used first for copying or moving the file(s), 
            and after cleaning this dictionary will be used for generating the report.
        fname : str
            Filename of the report.
        """
        f = open(f"{fname}.xml", "w+")
        f.write(dict2xml(copy_dict, wrap="all", indent="  "))
        f.close()


class HashTag:
    """Hash Generation of the current filename.

    Parameters
    ----------
    args : dict
        Dictionary of the keywords and values from the parser.

    Attributes
    ----------
    hname : str
        hash-secured filename.
    """

    hname = str

    def __init__(self, args):
        """Initialise the class."""
        self.args = args

    @staticmethod
    def fpath2hash(fpath, sha_key):
        """Transform regular expression into hash translated expression.

        Parameters
        ----------
        fpath : str
            Final path of the file name.
        sha_key : str
            Reference SHA key of the secured hash algorithm.

        Returns
        -------
        hcode: str
            Returns the encoded full path in hexadecimal format.
        """
        fpath_encoded = fpath.encode("utf-8")
        if sha_key == SHAKeys.sha1:
            #  deepcode ignore insecureHash: <because the option is needed>
            hcode = hlib.sha1(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha224:
            hcode = hlib.sha224(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha256:
            hcode = hlib.sha256(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha384:
            hcode = hlib.sha384(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha512:
            hcode = hlib.sha512(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.blake2b:
            hcode = hlib.blake2b(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.blake2s:
            hcode = hlib.blake2s(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.md5:
            #  deepcode ignore insecureHash: <because the option is needed>
            hcode = hlib.md5(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha3_224:
            hcode = hlib.sha3_224(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha3_256:
            hcode = hlib.sha3_256(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha3_384:
            hcode = hlib.sha3_384(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.sha3_512:
            hcode = hlib.sha3_512(fpath_encoded)
            return hcode.hexdigest()
        elif sha_key == SHAKeys.shake_128:
            hcode = hlib.shake_128(fpath_encoded)
            return hcode.hexdigest(32)
        elif sha_key == SHAKeys.shake_256:
            hcode = hlib.shake_256(fpath_encoded)
            return hcode.hexdigest(32)

    def make_full_hashname(self, hpath, suffix, sha_key):
        """Make the full hash-secured filename.

        Parameters
        ----------
        hpath : str
            The full hash-secured filename.
        suffix : str
            The standard file-extension.
        sha_key : str
            SHA-key used as prefix or file-extension. 

        Returns
        -------
        hname : str
            The full hash-secured filename with optional suffixes in as prefix or file 
            extension. 
        """
        if self.args["no_file_extension"]:
            return hpath

        if (
            not self.args["no_file_extension"]
            and not self.args["file_extension"]
            and not self.args["file_suffix"]
        ):
            return "{}{}".format(hpath, suffix)
        if self.args["file_extension"]:
            hpath = "{}.{}".format(hpath, sha_key)
        if self.args["file_suffix"]:
            hpath = "{}-{}".format(sha_key, hpath)
        return hpath

    def generate_hashname(self, fname, suffix, sha_key):
        """Generate the hashname of the filename.

        generate_hashname() generates for a given filename and a given reference key, 
        the encoded filename in hexadecimal format.

        Parameters
        ----------
        fname : str
            Filename, which has to be translated to hash-secured filename.
        suffix : str
            File-extension of the filename.
        sha_key : str
            Reference key for selection the corresponding secured hash algorithm.

        Returns
        -------
        hname: str
            hash-secured filename.
        
        Notes
        -----
            1. The full-path will be encoded in in hexadecimal format by using a
                reference secure hash algorithms (sha) from `hashlib`.
            2. The new hashname will be normally merged with the standard suffix (file 
                extension) from the reference filename. The suffix can be optional:
                a. Remove any file-extension.
                b. Replaced by the abbreviation of the used secure hash algorithms 
                   (sha).
                c. Removed the standard file-extension and add the used secure hash 
                   algorithms (sha) in front of the new hashname seperated by a colon.
        """
        hpath = self.fpath2hash(fname, sha_key)
        self.hname = self.make_full_hashname(hpath, suffix, sha_key)

        return self.hname


class Copy2Hash(ExportReport, HashTag):
    """Copy or move file(s) to hash-secured named file(s).
    
    The Copy2Hash() class is 

    Parameters
    ----------
    ExportReport : class
        Class for generating the report of the file(s) copying or moving for retracing
        regular filename(s) with the new generated filenames(s)
    HashTag : class
        Class for generating the hash-secured names for the files to copy or moving the 
        files to hash-secured filename(s)
    args : dict
            Dictionary of the keywords and values from the parser
    
    Attributes
    ----------
    _copy_dir : dir
       Internal dictionary will be used first for copying or moving the file(s), and 
       after cleaning this dictionary will be used for generating the report. 
    """

    def __init__(self, args):
        """Initialise the class with super."""
        super().__init__(args)
        self.args = args
        self._copy_dir = {
            "index": [],
            "filename": [],
            "ppath": [],
            "fpath": [],
            "suffix": [],
            "mode": [],
            "home_dir": [],
            "copy_dir": [],
        }

    @staticmethod
    def deconvolute_path(fname):
        """Deconvoulte the filename into the dir, name, ext.

        Parameters
        ----------
        fname : str
            Current filename including the parent directory.

        Returns
        -------
        ppath : str
            Parent path of the current file.
        fpath : str
            Final path of the current file.
        suffix : str
            File-extension of the current file.
        fname : str
            Filename of the current filename without the parent path.
        """
        # Deconvulute full directory and file path
        ppath = Path(fname).parent
        fpath = Path(fname).stem
        suffix = Path(fname).suffix
        # file name with file-extension
        fname = Path(fname).name
        return ppath, fpath, suffix, fname

    @staticmethod
    def get_copypath(s_ppath, args):
        """Get the path to copy or move the file(s).

        get_copypath() checks if the copy directory is equal to the home directory 
        (`./`), if not it replaced the home directory by the new reference directory.

        Parameters
        ----------
        args : dict
            Dictionary of the keywords and values from the parser.
        fname : str
            Filename of current datafile to copy.

        Returns
        -------
        s_ppath: str
            Standard parents path for copying of moving the hash-secured files from 
            './' to './'.
        n_ppath: str, optional
            New parents path for copying of moving the hash-secured files from './' 
            to './directory'.
        """
        directory = args["directory"]
        if args["directory"]:
            n_ppath = Path(args["directory"])
            if not directory.is_dir():
                directory.mkdir(parents=True, exist_ok=True)
                if args["verbose"]:
                    log(f"Made new directory {directory}!", 2)
            return s_ppath.as_posix(), n_ppath.as_posix()
        return s_ppath.as_posix(), s_ppath.as_posix()

    def find_files(self):
        """Get the filenames and save it.

        find_files() reads the filenames and the working mode to an internal dictionary.
        This is part I of II, because get_hash() has to add the hash-keys according to 
        the number of selected SHA keys in the parser. 
        """
        for i, fname in enumerate(self.args["infile"]):
            self._copy_dir["index"].append(i)
            ppath, fpath, suffix, fname = self.deconvolute_path(fname)
            self._copy_dir["filename"].append(fname)
            self._copy_dir["ppath"].append(ppath)
            self._copy_dir["fpath"].append(fpath)
            self._copy_dir["suffix"].append(suffix)

            if self.args["move"]:
                self._copy_dir["mode"].append("move")
            else:
                self._copy_dir["mode"].append("copy")

            s_ppath, n_ppath = self.get_copypath(ppath, self.args)
            self._copy_dir["home_dir"].append(s_ppath)
            self._copy_dir["copy_dir"].append(n_ppath)

    def transform_hash(self):
        """Get the hash-secured file names.

        transform_hash() transform the regular filename(s) to a hash-secured 
        filename(s). It adds the new hash-secured filename(s) and their export 
        directory to the _copy_dir directory.

        Notes
        -----
        In the old version, just the filename (self._copy_dir["fpath"]) without file 
        extension was used, but this is problematic in cases of equal filenames with 
        different extension. Now, the full filename (self._copy_dir["filename"]) are
        used. 
        """
        for i, sha_key in enumerate(self.args["sha"]):
            sha_fname = []
            for (fname, suffix) in zip(
                self._copy_dir["filename"], self._copy_dir["suffix"]
            ):
                hname = self.generate_hashname(fname, suffix, sha_key)
                sha_fname.append(hname)
            self._copy_dir[sha_key] = sha_fname

    def copy_files(self):
        """Copy regular named file(s) to hash-secured named file(s)."""
        sha_key_list = list(self._copy_dir.keys())[8:]

        for filename, home_path, copy_path in zip(
            self._copy_dir["filename"],
            self._copy_dir["home_dir"],
            self._copy_dir["copy_dir"],
        ):
            for sha_key in sha_key_list:
                for copyname in self._copy_dir[sha_key]:
                    try:
                        copy(
                            Path(home_path).joinpath(filename),
                            Path(copy_path).joinpath(copyname),
                        )
                        if self.args["verbose"]:
                            log(
                                "Copy file '{}/{}' \n\tto '{}/{}'".format(
                                    home_path, filename, copy_path, copyname
                                ),
                                2,
                            )
                    except FileNotFoundError as e_1:
                        log(msg=f"{e_1}", mode=3)
                        pass
                    except IsADirectoryError as e_2:
                        log(msg=f"{e_2}", mode=3)
                        pass
                    except SameFileError as e_3:
                        log(msg=f"{e_3} -> will not be replaced!", mode=3)
                        pass

    def move_files(self):
        """Move regular named file(s) to hash-secured named file(s)."""
        sha_key_list = list(self._copy_dir.keys())[8:]
        if len(sha_key_list) > 1:
            sha_key = sha_key_list[0]
            log("SHA key list is >1; only the first will be picked!", 3)
        else:
            sha_key = sha_key_list[0]
        for filename, home_path, move_path in zip(
            self._copy_dir["filename"],
            self._copy_dir["home_dir"],
            self._copy_dir["copy_dir"],
        ):
            for movename in self._copy_dir[sha_key]:
                try:
                    Path(home_path).joinpath(filename).rename(
                        Path(move_path).joinpath(movename)
                    )
                    if self.args["verbose"]:
                        log(
                            "Move file '{}/{}' \n\tto '{}/{}'".format(
                                home_path, filename, move_path, movename
                            ),
                            2,
                        )
                except FileNotFoundError as e_1:
                    log(msg=f"{e_1}", mode=3)
                    pass
                except IsADirectoryError as e_2:
                    log(msg=f"{e_2}", mode=3)
                    pass

    def clean_dict(self):
        """Remove unnecessary entries in the dictionary."""
        del self._copy_dir["ppath"]
        del self._copy_dir["fpath"]
        del self._copy_dir["suffix"]

    def copy2hash(self):
        """Copy or move the file(s) to hash renamed file(s).
        
        Attributes
        ----------
        1. self.find_files() -> find the file(s)
        2. self.transform_hash() -> generate the hash names for the file(s)
        3. move or copied the file(s) -> 
        4. Remove unnecessary entries in the dictionary -> self.clean_dict()
        5. make a report with of the copied or moved file(s) ->  self.make_export
        """
        self.find_files()
        self.transform_hash()
        if self.args["move"]:
            self.move_files()
        else:
            self.copy_files()
        self.clean_dict()
        self.make_export(self._copy_dir)


def get_args(opt=None):
    """Get the parser arguments from the command line.
    
    Returns
    -------
    args : dict
        Dictionary of the keywords and values from the parser.

    Parameters
    ----------
    opt : dict, optional
        Optional Dictionary for modifying the parser arguments; default is None.
    """
    parser = argparse.ArgumentParser(
        description=(
            "copy or rename any file(s) to a hash-secured filename via terminal"
        )
    )
    # Arguments for loading the data
    parser.add_argument(
        "infile",
        nargs="*",
        type=str,
        help=(
            "file(s) to copy or to rename with regular filename to secured hash "
            "filename"
        ),
    )
    parser.add_argument(
        "-r",
        "--report",
        help=(
            "define one or a series of file format(s) for the rename-report(s) to "
            "retrace the copying or rename of the file(s). The availabel file formats "
            "are:'csv', 'json', 'pkl', 'txt', 'yaml', 'xml', or own file-extension as "
            "ASCII; default is 'json'"
        ),
        default=["json"],
        nargs="*",
        type=str,
    )
    parser.add_argument(
        "-rn",
        "--report_name",
        help=(
            "define the report name for the copied or move file(s); default is "
            "'copy_report'"
        ),
        default="copy_report",
        type=str,
    )
    parser.add_argument(
        "-s",
        "--sha",
        help=(
            "define one or a series of secure hash algorithms (sha) for copying or "
            "rename of the file(s). The availabel secure hash algorithms (sha) are: "
            "'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', "
            "'md5', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', "
            "'shake_256'; default 'sha256'. The 'shake_128' and 'shake_256' are "
            "defined for 32 character length."
        ),
        default=["sha256"],
        nargs="*",
        type=str,
    )
    parser.add_argument(
        "-dir",
        "--directory",
        help=(
            "replace the standard directory ('./') by a specific directory ('./path). "
            "If the specific directory not exist, the directory will be created. This "
            "can required sudo rights."
        ),
        default=None,
        type=str,
    )
    parser.add_argument(
        "-mv",
        "--move",
        help=(
            "moving the file(s) instead of copying the files with regular filename to "
            "secure hash filename"
        ),
        action="store_true",
    )
    parser.add_argument(
        "-fxt",
        "--file_extension",
        help=(
            "replaced the given file-extension by the abbreviations of the used secure "
            "hash algorithms (sha)"
        ),
        action="store_true",
    )
    parser.add_argument(
        "-sxt",
        "--file_suffix",
        help=(
            "removed the given file-extension and add a suffix in front of the file "
            "based on the abbreviations of the used secure hash algorithms (sha). It "
            "is seperated by colon like "
            "'sha256-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'"
        ),
        action="store_true",
    )
    parser.add_argument(
        "-nfxt",
        "--no_file_extension",
        help=(
            "removed the any file-extension and just copy or move the file(s) as sha "
            "renamed file(s)"
        ),
        action="store_true",
    )
    parser.add_argument(
        "-ver", "--verbose", help=("enable the verbose mode"), action="store_true"
    )
    parser.add_argument(
        "-v",
        "--version",
        help=("displays the current version of cop2hash"),
        action="store_true",
    )

    args = vars(parser.parse_args())

    # For pytest
    if opt:
        for item, value in opt.items():
            args[item] = value

    return args


def command_line_runner(opt=None):
    """Run bashplot() via command line.
    
    Parameters
    ----------
    opt : dict, optional
        Optional Dictionary for modifying the parser arguments; default is None.
    """
    args = get_args()

    # For pytest
    if opt:
        for item, value in opt.items():
            args[item] = value

    if args["version"]:
        log(__version__)

    if not args["infile"]:
        log("Missing input file(s)!", mode=1)
        return

    if args["directory"]:
        args["directory"] = Path(args["directory"])

    if not set(args["sha"]).issubset(SHAKeys.__dict__):
        log("No legal SHA-key(s) {}!".format(args["sha"]), 1)
        return

    if args["verbose"]:
        msg = "Found following files:\n{}".format("\n".join(str(args["infile"])))
        log(msg=msg, mode=2)

    Copy2Hash(args).copy2hash()


if __name__ == "__main__":
    command_line_runner()
