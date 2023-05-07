import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1010))


msg = s.recv(1024).decode()
s.send(input(msg).encode())
msg = s.recv(1024).decode()
s.send(input(msg).encode())

print(s.recv(1024).decode())

