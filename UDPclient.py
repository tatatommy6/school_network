import socket
BUFFSIZE = 1024
port=2500
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addr=input("Server IP Address: ")
if ip_addr=="":
    ip_addr="localhost"
addr=(ip_addr,port)

while True:
    msg=input("<-")
    s.sendto(msg.encode(),addr)
    print("->", end='')
    data, addr=s.recvfrom(BUFFSIZE)
    print(data.decode())