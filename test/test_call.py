import subprocess
import copy2hash


class TestTerminal(object):
    def test_terminal_version(self):

        result = subprocess.check_output(["copy2hash", "test/example1.txt", "-v"])

        assert result == str.encode(f"{copy2hash.__version__}\n")

    def test_terminal_help(self):

        result = subprocess.call(["copy2hash", "-h"])

        assert not result

    def test_terminal_nofile(self):

        result = subprocess.call(["copy2hash"])

        assert not result
