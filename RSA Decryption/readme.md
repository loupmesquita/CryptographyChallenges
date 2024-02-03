# RSA Decryption of a ciphertext

A text has been encrypted using the PKCS1_OAEP algorithm. However, we have the public key with which it has been encrypted and P which is one the prime number used to encrypt using RSA


## How to proceed

We have to know that the public key contains e and n important elements for the algorithm used in this encryption.

So the first step is to try to find e and n from the pem.

A python script "extract_pem.py" was made for this purpose.

Now with these 3 components, we can go through all the steps to find the private key

After that, with that private key, we can use different python libraries like Cryptography and PyCryptodome to decrypt the ciphertext.