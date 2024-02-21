from click.testing import CliRunner

from gull.cli import gull


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(gull, ["Peter"])
    assert result.exit_code == 0
    assert result.output == "Hello Peter!\n"
