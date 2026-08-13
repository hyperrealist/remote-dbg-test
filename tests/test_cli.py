import subprocess
import sys

from remote_dbg_test import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "remote_dbg_test", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
