import pathlib

import xmlschema

SCHEMA_DIR = pathlib.Path(__file__).parent / "schemas"

order_schema = xmlschema.XMLSchema(
    str(SCHEMA_DIR / "STAND013-Order_Interchange_v1p1.xsd")
)
order_response_schema = xmlschema.XMLSchema(
    str(SCHEMA_DIR / "STAND013-OrderResponse_Interchange_v1p1.xsd")
)
delivery_note_schema = xmlschema.XMLSchema(
    str(SCHEMA_DIR / "STAND013-DeliveryNote_Interchange_v1p1.xsd")
)
