#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto import Random
import base64, sys, hashlib

base = 16

syntax_msg = """
Syntax:
  To encrypt:  ./AESCipher -e <input_file> <output_file>
  To decrypt:  ./AESCipher -d <input_file> <output_file>
"""

class AESCipher:

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.base = 16

    def padString(self, origin_string):
        return origin_string + (self.base - len(origin_string) % self.base) * chr(self.base - len(origin_string) % self.base)

    def unpaddString(self, padded):
        return padded[:-ord(padded[len(padded)-1:])]
    
    def encrypt(self, inputfile, outputfile):
        file = open(inputfile,'r')
        if not file:
            print("The input file is invalid")
            sys.exit(1)
        raw = file.read()
        file.close()
        padded_raw = self.padString(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        encrypted = iv + cipher.encrypt(padded_raw)
        encrypted = hashlib.sha256(encrypted).digest() + encrypted
        new_file = open(outputfile,'wb')
        new_file.write(encrypted)
        new_file.close()

    def decrypt(self, inputfile, outputfile):
        file = open(inputfile,'rb')
        if not file:
            print("The input file is invalid")
            sys.exit(1)
        encrypted = file.read()
        file.close()
        signature = encrypted[:32]
        encrypted = encrypted[32:]
        if signature != hashlib.sha256(encrypted).digest():
            print("The encrypted message is tampered!!!")
            sys.exit(1)
        iv = encrypted[:16]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        padded_decrypted = cipher.decrypt(encrypted[16:])
        if not padded_decrypted:
            print("The secret key is wrong!!!")
            sys.exit(1)
        decrypted = str(self.unpaddString(padded_decrypted), 'utf-8')
        new_file = open(outputfile,'w')
        new_file.write(decrypted)
        new_file.close()


def main():
        if len(sys.argv) is not 4:
                print(syntax_msg)
                sys.exit(1)
        secret_key = input("Enter your secret key: ")
        myCipher = AESCipher(secret_key)
        
        if sys.argv[1] == "-e":
            myCipher.encrypt(sys.argv[2], sys.argv[3])
        else:
            myCipher.decrypt(sys.argv[2], sys.argv[3])
        


if __name__== "__main__":
        main()


