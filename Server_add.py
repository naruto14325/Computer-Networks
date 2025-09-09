import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen()

print("🔵 Server is listening on port 9999...")

conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Client disconnected.")
        break

    print(f"Client: {data}")

    reply = input("Server (enter number or 'exit'): ")
    conn.send(reply.encode())

    # Try to compute sum if both are integers
    try:
        client_num = int(data)
        server_num = int(reply)
        total = client_num + server_num
        print(f"🔢 Sum: {client_num} + {server_num} = {total}")
    except ValueError:
        print("⚠️ One of the values is not an integer. Skipping sum.")

conn.close()