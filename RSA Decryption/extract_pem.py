from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load the public key
with open("rsa1.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Get the modulus (n) and the public exponent (e)
n = public_key.public_numbers().n
e = public_key.public_numbers().e

print(f"Modulus (n): {n}")
print(f"Public Exponent (e): {e}")