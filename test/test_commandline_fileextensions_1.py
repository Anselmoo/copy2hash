from copy2hash import copy2hash
from pathlib import Path


def test_local_specific_file():
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
