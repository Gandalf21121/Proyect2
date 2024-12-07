from cryptography.fernet import Fernet

# Generate a valid key
key = Fernet.generate_key()
print("Generated Key:", key.decode())