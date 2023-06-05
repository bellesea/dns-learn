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

def parse_header(reader):
    items = struct.unpack("!HHHHHH", reader.read(12))
    return DNSHeader(*items)

reader = BytesIO(response)
print(parse_header(reader))