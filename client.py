
from http import server
import socket    

if __name__ == "__main__":
    ip = "127.0.0.1"
    port= 1234

    client  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    client.connect((ip,port))

    string = "GET / HTTP/1.1\nHost: localhost\n"
    client.send(bytes(string, "utf-8"))

