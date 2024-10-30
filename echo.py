import socket

port = 2500
BUFSIZE = 1024

dict={'1':'one','2':'two','3':'three'}
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=sock.bind(('0.0.0.0',port))
sock.listen(1)
print("waiting for connection...")
c_sock, addr = sock.accept()
print(f"Connected by {addr}")

while True:
    data = c_sock.recv(BUFSIZE).decode()
    if not data:
        break
    try:
        c_sock.send(dict(int[data]).encode())
    except:
        c_sock.send("try again".encode())
sock.close()
