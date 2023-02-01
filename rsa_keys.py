import rsa
import random

nodes = 4

# Generate a public/private key pair
def generate_keys(size=4):
    (pubkey, privkey) = rsa.newkeys(2**size)
    e = pubkey.e
    d = privkey.d
    n = pubkey.n
    return (e, d, n)

def setNodeSize(size):
    nodes = size

(e, d, n) = generate_keys()
message_binary = ""
phi = []


# Encrypt a message with a public key
def encrypt_message(message_binary_tuple=message_binary, e=e, n=n):
    message_binary = message_binary_tuple[0]
    message_binary_length = message_binary_tuple[1]
    (message_binary_padded,message_binary_array,message_binary_length) = formatBinaryStringToBytes(message_binary)
    message = toDecimalArray(message_binary_array)
    return [pow(data, e, n) for data in message]

# Decrypt a message with a private key
def decrypt_message(ciphertext, d=d, n=n):
    plain_array = [pow(char, d, n) for char in ciphertext]
    return (plain_array)

def toBinary(n):
    n_b = "{0:b}".format(n)
    plain_text = n_b[2:]
    plain_text_len = len(plain_text)
    plain_text = plain_text.zfill(len(plain_text) + (nodes - plain_text_len % nodes))
    return (plain_text, len(plain_text))

def generateRandomMessage(size=32):
    message_binary = toBinary(random.randint(0, 2**size - 1))
    return(message_binary)

message_binary = generateRandomMessage()

def toDecimal(n):
    return int(n, 2)

def toDecimalArray(n):
    return [int(i, 2) for i in n]

def formatBinaryStringToBytes(binary_string):
    plain_text_array = [binary_string[i:i+nodes] for i in range(0, len(binary_string), nodes)]
    return (binary_string , plain_text_array, len(binary_string))

def makeToi(x):
    phi = []
    for i in range(e):
        phi_ele = pow(x,i,n)
        if phi_ele not in phi:
            phi.append(phi_ele)
        else:
            return(len(phi), max(phi))


