from rsa_encryption import RSACipher

def main():
    RSACipher.make_keypair()
    msg = "this is a secret message"
    public_key = RSACipher.get_key('public.key')
    private_key = RSACipher.get_key('private.key')

    c = RSACipher()

    enc = c.encrypt(msg, public_key)

    print("======== 암호화 ========")
    print("평문: " + msg)
    print("암호문: " + str(enc))

    print("======== 복호화 ========")
    print("복호화 결과: " + c.decrypt(enc, private_key))

main()

    