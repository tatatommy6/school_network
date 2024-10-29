import socket
port=int(input("port no: "))
address=("192.168.31.66",port)
BUFSIZE=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(address)
while True:
    msg=input("Enter message: ")
    s.send(msg.encode())
    data=s.recv(BUFSIZE) 
    print(f"Received: {data.decode()}")