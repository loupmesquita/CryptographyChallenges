from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_message(n, ciphertext_file):
    p = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907
    e = 65537 

    # Calculate q and phi
    q = n // p
    phi = (p - 1) * (q - 1)

    # Calculate d
    d = inverse(e, phi)
    
    # Create the private key
   
    private_key = RSA.construct((n, e, d))

    # Load the message from a file
    with open(ciphertext_file, "rb") as file:
        ciphertext = file.read()

    cipher = PKCS1_OAEP.new(private_key)

    # Decipher the encrypted message
    plaintext = cipher.decrypt(ciphertext)

    # Show the encrypted message
    print("Message déchiffré :")
    print(plaintext.decode("utf-8"))



if __name__ == "__main__":
    n_hex = "008b030e7886d2bcbf0db951a02a1055ca6d9915c4647b1d95e0f08a93687a1c1ceef0b97e7c38dc6e72a832cdc2cc2ac8c852f6fb22d691587db97bdd4fd8504bfb8153def44f17995f7f645e588bf977593a3bc3126a332dbd482b0d99230cea6c37c33bc35524c61e4a521a314fafedf6f2c660ed3d15b695c7c3902be4ea7d"
    ciphertext_file = "rsa1Cipher.txt"

    n = int(n_hex, 16)

    decrypt_message(n, ciphertext_file)