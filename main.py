from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption

def generate_key_pair():
    # Membuat pasangan kunci DSA
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(private_key, message):
    # Menandatangani pesan dengan kunci privat DSA
    signature = private_key.sign(
        message,
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    # Memverifikasi tanda tangan dengan kunci publik DSA
    try:
        public_key.verify(
            signature,
            message,
            hashes.SHA256()
        )
        return True
    except dsa.InvalidSignature:
        return False

# Contoh penggunaan
private_key, public_key = generate_key_pair()
message_to_sign = b"Hello, World!"

# Tanda tangani pesan
signature = sign_message(private_key, message_to_sign)
print(f"Signature: {signature.hex()}")

# Verifikasi tanda tangan
is_verified = verify_signature(public_key, message_to_sign, signature)
if is_verified:
    print("Signature verification successful.")
else:
    print("Signature verification failed.")
