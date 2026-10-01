import socket

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started...")
print("Waiting for client...")

client_socket, address = server_socket.accept()

print("Client connected:", address)

client_socket.send("Hello from server".encode())

client_socket.close()
server_socket.close()