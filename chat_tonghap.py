import socket
MAX_BYTES=1024

def server(interface, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    print(f"waiting for client {s.getsockname()}")

    while True:
        print("Server <- Client: ", end='')
        data,addr=s.recvfrom(MAX_BYTES)
        print(data.decode())
        resp=input("Server -> Client: ")
        s.sendto(resp.encode(),addr)

def client(hostname, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((hostname, port))
    print(f"클라이언트 소켓 이름은 {s.getsockname()}입니다.")

    while True:
        msg=input("Server <- Client: ")
        s.send(msg.encode())
        print("Server -> Client: ", end='')
        data, addr=s.recvfrom(MAX_BYTES)
        print(data.decode())


if __name__=="__main__":
    mode=input("Select mode(S,C): ")
    servip=input("server ip:(defult: 127.0.0.1): ")
    if servip=="":
        servip="127.0.0.1"
    
    port= input("port(defult: 2500)")
    if port=="":
        port=2500

    if mode=="S":
        server(servip, int(port))
    else:
        client(servip, int(port))
