from copy2hash import copy2hash
from pathlib import Path


def test_local_specific_file():
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
