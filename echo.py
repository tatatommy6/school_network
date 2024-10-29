import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print(f'connected by {remotehost}:{remoteport}')
while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print(f"Recevied message: {data.decode()}")
    conn.send(data)
conn.close()