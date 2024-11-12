from socket import *
addr=('<broadcast>',10001)

s= socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(("", 10000))

while True:
    smsg=input("broadcast message: ")
    s.sendto(smsg.encode(),(addr))