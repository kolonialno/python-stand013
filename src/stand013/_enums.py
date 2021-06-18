from __future__ import annotations

from enum import Enum
from os import PathLike
from pathlib import Path
from typing import Optional, Union

from lxml import etree


class DocumentType(str, Enum):
    """Supported document types."""

    ORDERS = "ORDERS"
    ORDRSP = "ORDRSP"
    DESADV = "DESADV"

    @classmethod
    def detect(cls, path: Union[PathLike, str]) -> Optional[DocumentType]:
        """Attempt to detect the document type of the given file."""

        path = Path(path)

        try:
            tree = etree.parse(str(path))
        except etree.XMLSyntaxError:
            return None

        namespaces = {"s": "http://www.ean-nor.no/schemas/eannor"}
        if tree.xpath("/s:Interchange/s:Order", namespaces=namespaces):
            return cls.ORDERS
        if tree.xpath("/s:Interchange/s:OrderResponse", namespaces=namespaces):
            return cls.ORDRSP
        if tree.xpath("/s:Interchange/s:DeliveryNote", namespaces=namespaces):
            return cls.DESADV

        return None

    @property
    def xml_schema_path(self) -> Path:
        """Path to the document type's XML Schema."""
        SCHEMA_DIR = Path(__file__).parent / "schemas"
        return {
            DocumentType.ORDERS: (SCHEMA_DIR / "STAND013-Order_Interchange_v1p1.xsd"),
            DocumentType.ORDRSP: (
                SCHEMA_DIR / "STAND013-OrderResponse_Interchange_v1p1.xsd"
            ),
            DocumentType.DESADV: (
                SCHEMA_DIR / "STAND013-DeliveryNote_Interchange_v1p1.xsd"
            ),
        }[self]
