import random
import base64
import hashlib
import sys

GP_TUPLE = [
        (1024, 160),
        (2048, 224),
        (2048, 256),
        (3072, 256)
    ]

def generate_int():
    return 0

def generateKey():
    GP_pair = GP_TUPLE[generate_int()] 
    
    Xa = 100
    Xb = 200

    A = (GP_pair[0]**Xa) % GP_pair[1]
    B = (GP_pair[0]**Xb) % GP_pair[1]

    keyA = (B**Xa) % GP_pair[1]
    keyB = (A**Xb) % GP_pair[1]

    hashA = hashlib.sha256(str(keyA).encode('utf-8')).hexdigest()
    hashB = hashlib.sha256(str(keyB).encode('utf-8')).hexdigest()

    print('Key A : ',hashA)
    print('Key B : ',hashB)

    return hashA, hashB