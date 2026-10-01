import socket

HOST = "10.110.36.33"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = input("Enter message: ")

client.sendall(message.encode())

data = client.recv(1024)

print("Echo from server:", data.decode())

client.close()