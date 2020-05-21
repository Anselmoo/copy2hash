from copy2hash import copy2hash
from pathlib import Path

__refargs__ = {
    "infile": [],
    "report": ["json"],
    "report_name": "copy_report",
    "sha": ["sha256"],
    "directory": None,
    "move": False,
    "file_extension": False,
    "file_suffix": False,
    "no_file_extension": False,
    "verbose": False,
    "version": False,
}


class TestParser(object):
    def test_parser(self):

        assert __refargs__ == copy2hash.get_args(opt=__refargs__)

    def test_parser_txt(self):

        fnames = Path("test").glob("*.txt")
        args = __refargs__
        args["infile"] = fnames

        assert args == copy2hash.get_args(opt=args)

    def test_parser_all(self):

        fnames = Path("test").glob("*")
        args = __refargs__
        args["infile"] = fnames

        assert args == copy2hash.get_args(opt=args)

    def test_parser_version(self):

        fnames = Path("test").glob("*")
        args = __refargs__
        args["infile"] = fnames

        assert args == copy2hash.get_args(opt=args)


class TestCommandLine(object):
    def test_nofiles(self):

        args = __refargs__
        args["infile"] = []
        copy2hash.command_line_runner(opt=args)
        assert 1

    def test_local_directory(self):

        args = __refargs__
        args["infile"] = ["."]
        copy2hash.command_line_runner(opt=args)
        assert 1
