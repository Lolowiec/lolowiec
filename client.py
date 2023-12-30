from http import server
import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    request = "GET / HTTP/1.1\nHost: GET localhost\n"
    client.send(bytes(request, "utf-8"))
