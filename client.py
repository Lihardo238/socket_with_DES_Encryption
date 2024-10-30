import socket
from cryptography.fernet import Fernet

key = input("Enter the shared encryption key: ").encode()
cipher = Fernet(key)

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Enter the message to encrypt and send: ").encode()

    encrypted_message = cipher.encrypt(message)
    print(f"Encrypted message: {encrypted_message}")

    client_socket.send(encrypted_message)
    client_socket.close()

start_client()
