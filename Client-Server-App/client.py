import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

print("Connected to the server. Type 'exit' to leave.")

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'exit':
        break

    reply = client_socket.recv(1024).decode()
    if reply.lower() == 'exit':
        print("Server ended the chat.")
        break
    print("Server:", reply)

client_socket.close()
