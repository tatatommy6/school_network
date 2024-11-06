import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.31.66"
port=2500
BUFSIZE=1024
s.connect((host, port))
s.send("i`m ready".encode())
fn=s.recv(1024).decode()

with open('recv/{filename}.txt'+fn, 'wb') as f:
    print("file opened ")
    print("receiving file...")
    while True:
        data=s.recv(8192)
        if not data:
            break
        f.write(data)
print('download complete')
s.close()
print('connection closed')