from __future__ import annotations

from os import PathLike
from pathlib import Path

from xmlschema import XMLSchema
from xmlschema.validators.exceptions import XMLSchemaValidationError

from stand013 import DocumentType

__all__ = [
    "validate",
    "XMLSchemaValidationError",
]


def validate(document_type: DocumentType, path: PathLike) -> None:
    path = Path(path)
    xml_schema = XMLSchema(str(document_type.xml_schema_path))
    xml_schema.validate(str(path))
