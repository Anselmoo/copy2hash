from copy2hash import copy2hash
from pathlib import Path


class TestSingleRuns(object):
    def test_all_reports(self):
        args = {
            "infile": list(Path("test").glob("example1.txt")),
            "report": ["csv", "json", "pkl", "yaml", "txt", "xml", "out"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": "home_home",
            "move": False,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_local_specific_files(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": False,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": False,
            "version": True,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_all_sha_keys(self):
        args = {
            "infile": list(Path("test").glob("example1.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": [
                "sha1",
                "sha224",
                "sha256",
                "sha384",
                "sha512",
                "blake2b",
                "blake2s",
                "md5",
                "sha3_224",
                "sha3_256",
                "sha3_384",
                "sha3_512",
                "shake_128",
                "shake_256",
            ],
            "directory": None,
            "move": False,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_move_local_files_verbose(self):
        args = {
            "infile": list(Path("test").glob("example1.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": True,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1
    
    def test_move_local_files(self):
        args = {
            "infile": list(Path("test").glob("example1.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": True,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1
    
    def test_move_local_files_directory(self):
        args = {
            "infile": list(Path("test")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": True,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1
    
    def test_local_wrong_sha(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha713"],
            "directory": None,
            "move": False,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": False,
            "version": True,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1
