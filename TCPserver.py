import socket

port = 2500
host = "0.0.0.0"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
print("waiting for connection...")
c_sock, addr = sock.accept()

print(f"Connected by {addr}")
data = c_sock.recv(1024)
print(data.decode())
filename = input("file name to send: (c:/test/sample.bin) ")

print(f"sending {filename}...")
fn = filename.split("/")
c_sock.sendall(fn[-1].encode())

with open(filename, "rb") as f:
    c_sock.sendfile(f, 0)

print("sending complete")
c_sock.close()
sock.close()