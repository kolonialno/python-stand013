# python-stand013

python-stand013 is a Python app and library for parsing, writing, and validation
of the [STAND013](https://stand.no/) file format.

## Features

The following is a list of python-stand013's existing and planned features.

- Validation
  - [x] `ORDERS` purchase orders
  - [x] `ORDRSP` purchase order responses
  - [x] `DESADV` delivery notes
- Parsing
  - [ ] `ORDERS` purchase orders
  - [ ] `ORDRSP` purchase order responses
  - [ ] `DESADV` delivery notes
- Writing
  - [ ] `ORDERS` purchase orders
  - [ ] `ORDRSP` purchase order responses
  - [ ] `DESADV` delivery notes

## Installation

python-stand013 requires Python 3.7 or newer. It can be installed from PyPI using e.g. pip:

```
python3 -m pip install stand013
```

## Usage as command line tool

The `stand013` executable can be used to validate ORDERS, ORDRSP, and DESADV
files. The file type to validate is automatically detected.

Example of successful validation:

```
❯ stand013 validate tests/examples/ordrsp.xml
File: tests/examples/ordrsp.xml
Document type: ORDRSP
XML Schema validation: passed
❯
```

Example of unrecognized file format:

```
❯ stand013 validate /etc/passwd
File: /etc/passwd
Document type: Failed to detect
❯
```

Example of invalid file:

```
❯ stand013 validate DESADV-failing.xml
File: DESADV-failing.xml
Document type: DESADV
XML Schema validation: failed

  failed validating {} with XsdAttributeGroup(['MessageOwner', 'MessageType', 'MessageVersion']):

  Reason: missing required attribute 'MessageOwner'

  Schema:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="DeliveryNoteType">
      <xsd:sequence>
        <xsd:element name="MessageNumber" type="xsd:string" minOccurs="0">
          <xsd:annotation>
            <xsd:documentation>Unikt nr som identifiserer meldingen innenfor en utveksling</xsd:documentation>
          </xsd:annotation>
        </xsd:element>
        <xsd:element name="MessageTimestamp" type="xsd:dateTime">
          <xsd:annotation>
            <xsd:documentation>Meldingens dato (YYYY-MM-DDTHH:MM:SS) Sendetidspunkt</xsd:documentation>
          </xsd:annotation>
        </xsd:element>
        <xsd:element name="DeliveryNoteHeader" type="DeliveryNoteHeaderType">
          <xsd:annotation>
            <xsd:documentation>Pakkseddel hode</xsd:documentation>
          </xsd:annotation>
        </xsd:element>
        <xsd:element name="DeliveryNoteDetails" type="DeliveryNoteDetailsType" maxOccurs="unbounded">
          <xsd:annotation>
            <xsd:documentation>Pakkseddel detaljer</xsd:documentation>
      ...
      ...
    </xsd:complexType>

  Instance:

    <DeliveryNote xmlns="http://www.ean-nor.no/schemas/eannor">
      <MessageOwner>GS1NOR</MessageOwner>
      <MessageType>DELIVERYNOTE</MessageType>
      <MessageVersion>STAND013 v.1.0</MessageVersion>
      <MessageTimestamp>2021-05-31T09:49:00</MessageTimestamp>
      ...
      ...
    </DeliveryNote>

  Path: /Interchange/DeliveryNote

❯
```

## Usage as library

TODO: Pending support for parsing and writing STAND013 files.

## XML schema changes

The bundled XML schemas in `src/stand013/schemas/` have been retrieved from
https://stand.no/en/home/downloads/. We're currently including the May 2020
revision of the XML schemas.

We've done the following changes to the XML schemas to make them work for our use case.

- Commit 7bdb761d378a4ec2922a1ea14048b614e4cd08e1: Fix references to the
  `STAND013-Components_v1p1.xsd` file. This file is in the same directory as the
  other schemas, not in `../Components/`. This is true both for the Zip file at
  stand.no and in python-stand013.

- Commit bd9e138ac6275ccabe7ce0907157a3a83d0b5ea1: Renamed
  `STAND013 DeliveryNote_v1p1.xsd` to `STAND013-DeliveryNote_v1p1.xsd` so that
  the reference from `STAND013-DeliveryNote_Interchange_v1p1.xsd` works, and the
  file name matches the other XML schemas.

- Commit 955dfb86974d78f64d4da1dfdc72b0e27897a2a4: Change type for `ORDERS`'
  `Interchange/Order/OrderHeader/OrderResponse` from `MessageResponseType` (an
  enum with the values `AC`, `AE`, or `NE`) to a new `OrderResponseType` enum
  with `Z1` as the only possible value. This matches the format documentation,
  and is necessary to be able to validate any `ORDERS` using the XML schemas.

- Commit d6f6995642f9c60fcf039828a888df16f230f86c: Change required content for
  the `MessageVersion` element to be exactly `STAND013 v1.0` for `ORDERS`,
  `ORDRSP`, and `DESADV`. This matches the requirement in the field listings in
  the STAND013 documentation.
