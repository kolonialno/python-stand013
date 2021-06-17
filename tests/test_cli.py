from typer.testing import CliRunner

from stand013.cli import app

runner = CliRunner()


def test_validate_command() -> None:
    result = runner.invoke(app, ["validate", "--help"])
    assert result.exit_code == 0
    assert "Usage: stand013 validate" in result.stdout
