from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key_client, public_key_server):
    shared_key = private_key_client.exchange(public_key_server)
    return shared_key

def main():
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    parameters = server_public_key.parameters()
    private_key_client, public_key_client = generate_client_key_pair(parameters)

    shared_secret = derive_shared_secret(private_key_client, server_public_key)

    print(f"Shared Secret: {shared_secret.hex()}")

if __name__ == "__main__":
    main()