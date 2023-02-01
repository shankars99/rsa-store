import random
from rsa import newkeys as newkeys
from datatypes.dataoperations import *


def generate_keys(size: int = 4) -> Key:
    (pubkey, privkey) = newkeys(2**size)
    key = Key(pubkey.e, privkey.d, pubkey.n)
    return key


def createMessage(rand: bool = True, binary_string: str = "hello world", size: int = 32) -> BinaryString:
    if rand:
        return toBinary(random.randint(0, 2**size - 1))
    else:
        return formatBinaryStringToBytes(binary_string)

def modifyMessage(perc_start: float = 0.45, perc_end: float = 0.55) -> BinaryString:
    global message

    text = message.bin_val[:int(
        perc_start*message.bin_length)] + "0" + message.bin_val[int(perc_end*message.bin_length):]
    message = formatBinaryStringToBytes(text.zfill(message.bin_length))
    return message

key: Key = generate_keys()
data: DataObject = DataObject([], [], [])
message: BinaryString = createMessage(rand=True)
