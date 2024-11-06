import socket
port=2500
BUFFSIZE=1024
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print("waiting for client...")

while True:
    print("<-", end='')
    data,addr=s.recvfrom(BUFFSIZE)
    print(data.decode())

    resp=input("->")
    s.sendto(resp.encode(),addr)