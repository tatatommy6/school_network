from socket import *
s= socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("", 10001))
while True:
    msg,addr=s.recvfrom(1024)
    print(f"Received: {msg.decode()}")