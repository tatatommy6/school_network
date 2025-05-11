from socket import *
import struct
BUFFER=1024
gr_addr="224.0.0.255"
r=socket(AF_INET, SOCK_DGRAM)
r.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r.bind(("",5005 ))

mreq=struct.pack("4sl",inet_aton(gr_addr), INADDR_ANY)
r.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
print("ready to receive")

while True:
    data, addr=r.recvfrom(BUFFER)
    print(f"Received {data.decode()} from {addr}")
    r.sendto("ACK".encode(), addr)