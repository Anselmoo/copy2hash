#!/usr/bin/env python
"""copy2hash: Copy or rename any files to hash named files."""

######################################################
#
# copy2hash: - copying or rename files to hash secured
# files (sha) via the command line
# written by Anselm Hahn (Anselm.Hahn@gmail.com)
#
######################################################

import argparse
import hashlib as hlib
from pathspec import Path
import os
import sys

# imported fileformats
import csv
import json
import pickle
import yaml
import xml

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
        If mode is activated, message becomes an error message.
    """
    if mode:
        print(f"[ERROR] {msg}")
    else:
        print(msg)


if sys.version < "3.6":
    log("Unsupported Python Version (version < 3.6)!", 1)
    sys.exit(1)


class ExportReport:
    pass


class HashTag:
    pass


class CopyFile(ExportReport, HashTag):
    pass


def copy2hash(fnames, args):
    pass


def get_args(opt=None):
    """Get the parser arguments from the command line.
    
    Parameters
    ----------
    opt : dict, optional
        Optional Dictionary for modifying the parser arguments; default is None.
    
    Returns
    -------
    args : dict
        Dictionary of the keywords and values from the parser.
    """
    parser = argparse.ArgumentParser(
        description=(
            "copy or rename any file(s) to a hash secured filename via " "terminal"
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
        "-rp",
        "--report",
        help=(
            "define one or a series of file format(s) for the rename-report(s) to "
            "retrace the copying or rename of the file(s). The availabel file formats "
            "are: csv, json, pkl, txt, yaml, xml, or own file extension as ASCII; "
            "default is json"
        ),
        default="json",
        nargs="*",
        type=str,
    )
    parser.add_argument(
        "-s",
        "--sha",
        help=(
            "define one or a series of secure hash algorithms (sha) for copying or "
            "rename of the file(s). The availabel secure hash algorithms (sha) are: "
            "are: sha1, sha224, ssa256, sha384, sha512, blake2b, blake2s, md5, "
            "sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256; default "
            "sha256"
        ),
        default="sha256",
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
        "-fxt", "--file_extension", help=("replaced the given file extension by the "
        "abbreviations of the used secure hash algorithms (sha)"),
        action="store_false"
    )
    parser.add_argument(
        "-ver", "--verbose", help=("enable the verbose mode"), action="store_false"
    )
    parser.add_argument(
        "-v",
        "--version",
        help=("displays the current version of cop2hash"),
        action="store_true",
    )
    args = vars(parser.parse_args())
    if opt:
        for item, value in opt.items():
            args[item] = value
    return args


def command_line_runner():
    """Run bashplot() via command line."""
    args = get_args()

    if args["version"]:
        log(__version__)

    if not args["infile"]:
        log("Missing input file(s)!", mode=1)
        return

    fnames = args["infile"]
    copy2hash(fnames, args)


if __name__ == "__main__":
    command_line_runner()
