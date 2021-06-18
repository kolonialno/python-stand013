from pathlib import Path

import pytest

from stand013 import DocumentType

EXAMPLES_DIR = Path(__file__).parent / "examples"


@pytest.mark.parametrize(
    "example_file, document_type",
    [
        ("orders.xml", DocumentType.ORDERS),
        ("ordrsp.xml", DocumentType.ORDRSP),
        ("desadv.xml", DocumentType.DESADV),
    ],
)
def test_type_detection(example_file: str, document_type: DocumentType) -> None:
    path = EXAMPLES_DIR / example_file

    assert DocumentType.detect(path) == document_type


def test_type_detection_fails_on_unknown_file() -> None:
    assert DocumentType.detect(__file__) is None


def test_type_detection_fails_on_unknown_xml_file() -> None:
    assert DocumentType.detect(EXAMPLES_DIR / "unknown.xml") is None
