from pathlib import Path

import pytest

from stand013 import DocumentType, validation

EXAMPLES_DIR = Path(__file__).parent / "examples"


@pytest.mark.parametrize(
    "document_type, example_file",
    [
        (DocumentType.ORDERS, "orders.xml"),
        (DocumentType.ORDRSP, "ordrsp.xml"),
        (DocumentType.DESADV, "desadv.xml"),
    ],
)
def test_validate_document(document_type: DocumentType, example_file: str) -> None:
    path = EXAMPLES_DIR / example_file

    validation.validate(document_type, path)
