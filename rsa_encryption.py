from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSACipher:
    @staticmethod
    def make_keypair():
        private_key = RSA.generate(2048)
        print(private_key)

        public_key = private_key.publickey()
        print(public_key)

        pr_file = open('private.key','wb')
        pr_file.write(private_key.exportKey('PEM'))
        pr_file.close()

        pu_file = open('public.key', 'wb')
        pu_file.write(public_key.exportKey('PEM'))
        pu_file.close()

    def encrypt(self, msg, pu_key):
        tool = PKCS1_OAEP.new(pu_key)
        enc = tool.encrypt(msg.encode())
        return enc
    
    def decrypt(self, msg, pr_key):
        tool = PKCS1_OAEP.new(pr_key)
        dec = tool.decrypt(msg)

        return dec.decode("utf-8")
    
    @staticmethod
    def get_key(path):
        file = open(path, 'rb')
        key = RSA.import_key(file.read())
        return key
