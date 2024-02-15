from click.testing import CliRunner

from seal.cli import seal


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(seal, ["Peter"])
    assert result.exit_code == 0
    assert result.output == "Hello Peter!\n"
