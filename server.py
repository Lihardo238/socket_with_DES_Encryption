import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def start_server():
    host = 'localhost'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}")
    print(f"Encryption key (shared with client): {key.decode()}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        encrypted_message = conn.recv(1024)
        print(f"Encrypted message received: {encrypted_message}")
        
        decrypted_message = cipher.decrypt(encrypted_message)
        print(f"Decrypted message: {decrypted_message.decode()}")
        
        conn.close()
        break  

start_server()
