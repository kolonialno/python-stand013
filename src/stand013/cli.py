from pathlib import Path

import typer
import xmlschema

from stand013 import validation

app = typer.Typer()


@app.command()
def validate(filename: Path) -> None:
    path = str(filename.resolve())

    typer.secho(f"Validating {path} ...", bold=True)
    typer.echo()

    try:
        validation.order_response_schema.validate(path)
    except xmlschema.validators.exceptions.XMLSchemaValidationError as exc:
        typer.secho("XML Schema validation failed", bold=True, fg="red")
        typer.echo("")
        typer.echo(exc)
        raise typer.Exit(code=1)
    else:
        typer.secho("XML Schema validation passed", bold=True, fg="green")


@app.callback()
def callback() -> None:
    # XXX: Workaround to ensure the single command above is a sub-command.
    pass
