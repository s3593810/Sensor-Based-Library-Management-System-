# AES 256 encryption/decryption using pycrypto library
# Reference:https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html 
# That for learning purposes
 
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

class Security:
    """
    A class used to check errors and validations

    ...

    Attributes
    ----------
    BLOCK_SIZE : global
        a formatted string to print out what the animal says
    pad : global
        during registration it helps checking the inserted name errors.
    unpad : global
        during userName insertion it helps checking the validity with 
        defined charecters in the username.
    
    Methods
    -------
    encrypt(raw, password)
        takes in raw password from user and encrypts it to save in the database table
        to ensure data security.

    decrypt(enc, password)
        This method helps decyphering the password to check if that password belongs
        to a particular user or not.
    """
 
    global BLOCK_SIZE
    BLOCK_SIZE = 16
    global pad 
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    global unpad 
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self,raw, password):
        """
        Parameters
        ----------
        raw : str
            raw password typed by the user

        password : str
            encrypted password.
        
        """
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
    
    
    def decrypt(self,enc, password):
        """
        Parameters
        ----------
        enc : str
            Encrypted password from the database table
        password : str
            Decyphered password from the database table using 
            dycription mechanism.
        
        """
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))
