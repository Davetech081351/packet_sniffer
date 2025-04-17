import hashlib

# Input data to hash
data = input("Enter the text to hash: ")

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Encode the data and update the hash object
hash_object.update(data.encode())

# Get the hexadecimal digest of the hash
hash_digest = hash_object.hexdigest()

# Print the result
print(f"SHA-256 Hash: {hash_digest}")
