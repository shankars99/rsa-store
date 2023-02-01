from dataclasses import dataclass


@dataclass
class BinaryString:
    bin_val: str
    bin_array: list[str]
    bin_length: int
    int_array: list[int]


@dataclass
class Key:
    e: int
    d: int
    n: int


@dataclass
class DataObject:
    plain_text: list[int]
    encrypted_text: list[int]
    decrypted_text: list[int]
