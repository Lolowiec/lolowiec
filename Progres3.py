
from http import server
import socket    

if __name__ == "__main__":
    ip = "127.0.0.1"
    port= 1234

    server  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.connect((ip,port))