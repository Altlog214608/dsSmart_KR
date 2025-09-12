from cryptography.fernet import Fernet

key = b'b9O8keo9Fl-8Kl-IbvXuQ450cKCP0tXL8GRCqWxVSYw='
pw_init = "gAAAAAAAAAAAvcAsFofXR7XlzNv5B6-g-r0kyXVhvgzOyZJvJl2Khn_vOp_Q5OFYpw2yYdOnlbYdFctIdl_sc11ef3iWCjtx_xoGF48eT_DVAeHHcl1IFL0="
iv = b'\xbd\xc0,\x16\x87\xd7G\xb5\xe5\xcc\xdb\xf9\x07\xaf\xa0\xfa'
cipher = Fernet(key)

# 암호화
def encryptMessageVar(message):
    encrypted = cipher.encrypt(message.encode()).decode()
    print("암호화:", encrypted)
    return encrypted

# 암호화 고정
def encryptMessage(message):
    encrypted = cipher._encrypt_from_parts(message.encode(), 0, iv).decode()
    print("암호화:", encrypted)
    return encrypted

# 복호화
def decryptMessage(encryptedMessage):
    decrypted = cipher.decrypt(encryptedMessage).decode()
    print("복호화:", decrypted)
    return decrypted

if __name__ == "__main__":
    # msg = "!digitalscent1234"
    msg = ""
    enmsg = encryptMessage(msg)
    demsg = decryptMessage(pw_init)
    enmsgsame = encryptMessageVar(msg)
    demsgsame = decryptMessage(enmsgsame)
