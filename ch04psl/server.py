import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()

print("Server dinliyor: 127.0.0.1:5000")

conn, addr = server.accept()
print("Bağlanan:", addr)

data = conn.recv(1024)
print("Gelen veri:", data.decode())

conn.sendall(b"Merhaba client")

conn.close()
server.close()