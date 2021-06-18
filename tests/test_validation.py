from pathlib import Path

import pytest

from stand013.validation import DocumentType

EXAMPLES_DIR = Path(__file__).parent / "examples"


@pytest.mark.parametrize(
    "doc",
    [
        "orders.xml",
        "ordrsp.xml",
        "desadv.xml",
    ],
)
def test_validate_document(doc: str) -> None:
    path = EXAMPLES_DIR / doc

    document_type = DocumentType.detect(path)
    document_type.xml_schema.validate(str(path))
