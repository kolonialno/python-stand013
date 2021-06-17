import textwrap
from pathlib import Path

import typer

from stand013.validation import DocumentType, XMLSchemaValidationError

app = typer.Typer(name="stand013")


@app.command()
def validate(path: Path) -> None:  # pragma: no cover
    typer.secho(f"File: {path}")

    document_type = DocumentType.detect(path)
    if document_type is None:
        typer.secho("Failed to detect document type", bold=True, fg="red")
        raise typer.Exit(code=1)

    typer.secho(f"Document type: {document_type}")

    try:
        document_type.xml_schema.validate(str(path))
    except XMLSchemaValidationError as exc:
        typer.secho("XML Schema validation: failed", bold=True, fg="red")
        typer.echo("")
        typer.secho(textwrap.indent(str(exc), prefix="  "))
        raise typer.Exit(code=1)
    else:
        typer.secho("XML Schema validation: passed", bold=True, fg="green")


@app.callback()
def callback() -> None:  # pragma: no cover
    # XXX: Workaround to ensure the single command above is a sub-command.
    pass
