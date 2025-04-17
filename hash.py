import hashlib

file_path = input("Enter the file path: ")
try:
     with open(file_path, "rb") as f: # Open the file in binary mode
        file_content = f.read() # Read the file content md5_hash =
     hashlib.md5(file_content).hexdigest() # Calculate MD5 hash sha256_hash =
     hashlib.sha256(file_content).hexdigest() # Caculate SHA-256 hash

     print(f"MD5: {md5_hash}()")
     print(f"SHA256: {sha256_hash}")
except FileNotFoundError:
     print("File not found. Please check the path.")
