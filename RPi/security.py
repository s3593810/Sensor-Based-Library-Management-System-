# AES 256 encryption/decryption using pycrypto library
# Reference:https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html 
# That for learning perpuses
 
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

class Security:
 
    global BLOCK_SIZE
    BLOCK_SIZE = 16
    global pad 
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    global unpad 
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self,raw, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
    
    
    def decrypt(self,enc, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))
 
 
# # First let us encrypt secret message
# encrypted = encrypt("A123456", password)
 
# # Let us decrypt using our original password
# decrypted = decrypt(encrypted, password)
# bytes.decode(decrypted)
