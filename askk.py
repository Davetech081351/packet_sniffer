import hashlib

# Ask the user for a file path
file_path = input("Enter the file path to hash: ")

try:
  # Open the file in binary mode
  with open(file_path, "rb") as file:
     file_data = file.read()

     # Generate a SHA-256 hash of the file contents
     hash_digest = hashlib.sha256(file_data).hexdigest()
     print(f"SHA-256 File Hash: {hash_digest}")
except FileNotFoundError:
  print("File not found. Please check the file path.")
