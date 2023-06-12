from send import *
from dataclasses import dataclass
import struct 
from io import BytesIO

@dataclass
class DNSRecord:
    name: bytes
    type_: int
    class_: int
    ttl: int
    data: bytes

response = b'`V\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00R\x9b\x00\x04]\xb8\xd8"'

reader = BytesIO(response)
# question = reader.read(21)

def parse_header(reader):
    items = struct.unpack("!HHHHHH", reader.read(12))
    return DNSHeader(*items)

def decode_name_simple(reader):
    parts = []
    while (length := reader.read(1)[0]) != 0:
        parts.append(reader.read(length))
    return b".".join(parts)

def parse_question(reader):
    name = decode_name_simple(reader)
    data = reader.read(4)
    type_, class_ = struct.unpack("!HH", data)
    return DNSQuestion(name, type_, class_)

print(parse_question(reader))