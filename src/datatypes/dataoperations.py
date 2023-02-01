from src.datatypes.datatypes import *

nodes: int = 4


def toDecimal(n: str) -> int:
    return int(n, 2)


def toDecimalArray(n: list[str]) -> list[int]:
    return [toDecimal(i) for i in n]


def formatBinaryStringToBytes(binary_string: str) -> BinaryString:
    node_store_size = len(binary_string) // nodes
    plain_text_array: list[str] = [binary_string[i:i+node_store_size]
                                   for i in range(0, len(binary_string), node_store_size)]
    return (BinaryString(binary_string, plain_text_array, len(binary_string), toDecimalArray(plain_text_array)))


def toBinary(n) -> BinaryString:
    n_b = "{0:b}".format(n)
    plain_text = n_b[2:]
    plain_text_len = len(plain_text)
    plain_text = plain_text.zfill(
        len(plain_text) + (nodes - plain_text_len % nodes))
    return (formatBinaryStringToBytes(plain_text))
