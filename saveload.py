from cryptography.fernet import Fernet
def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()
def encrypt(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    encrypted = encrypted_message.decode()
    return encrypted
def decrypt(message):
    """
    Decrypts a message
    """
    encrypted_message = message.encode()
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    decrypted = decrypted_message.decode()
    return decrypted