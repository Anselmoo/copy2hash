from copy2hash import copy2hash
from pathlib import Path


class TestFileExtensions(object):
    def test_local_specific_file_i(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": False,
            "file_extension": True,
            "file_suffix": True,
            "no_file_extension": False,
            "verbose": False,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_local_specific_files_ii(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": False,
            "file_extension": True,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": False,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_local_specific_files_iii(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": False,
            "file_extension": False,
            "file_suffix": True,
            "no_file_extension": False,
            "verbose": False,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1

    def test_local_specific_file_iiii(self):
        args = {
            "infile": list(Path("test").glob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": False,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": True,
            "verbose": False,
            "version": False,
        }

        copy2hash.command_line_runner(opt=args)

        assert 1
