from pathlib import Path

from stand013.validation import DocumentType

EXAMPLES_DIR = Path(__file__).parent / "examples"


def test_validate_order() -> None:
    path = EXAMPLES_DIR / "orders.xml"

    document_type = DocumentType.detect(path)
    document_type.xml_schema.validate(str(path))
