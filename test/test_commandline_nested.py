from copy2hash import copy2hash
from pathlib import Path


class TestNestedDirectories(object):
    def test_local_nested_files_i(self):
        args = {
            "infile": list(Path("test").rglob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
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

    def test_local_nested_files_ii(self):
        # Double check concerning copy rights
        args = {
            "infile": list(Path("test").rglob("*.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
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

    def test_local_nested_files_iii(self):
        args = {
            "infile": list(Path("test").rglob("*.txt")),
            "report": ["csv", "json", "pkl", "yaml", "txt", "xml"],
            "report_name": "report4travis",
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

    def test_local_nested_files_iiii(self):
        # Double check concerning copy rights
        args = {
            "infile": list(Path("test").rglob("*.txt")),
            "report": ["csv", "json", "pkl", "yaml", "txt", "xml"],
            "report_name": "report4travis",
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
