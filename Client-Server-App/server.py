import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

server_socket.listen(1)
print("Waiting for a client to connect...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    message = conn.recv(1024).decode()
    if message.lower() == 'exit':
        print("Client left the chat.")
        break
    print("Client:", message)
    
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == 'exit':
        break

conn.close()
server_socket.close()
