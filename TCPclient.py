import socket
#tcp 소켓 생성
port=int(input("Enter port number: "))
sock=socket.create_connection(('192.168.31.20', port))

#데이터 전송
msg=input("Enter message: ")
print("Sending {}".format(msg))
sock.sendall(msg.encode())

#데이터 수신
data=sock.recv(1024)
print("received {}".format(data.decode()))
print("closing connection")

#소켓 닫기
sock.close()