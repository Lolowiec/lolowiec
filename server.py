#!/usr/bin/python3

import argparse
import socket

from httpserver import HttpRequest, HttpResponse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Httpserver',
        description='Working',
        epilog='Iam can t help you')

    parser.add_argument('-i', '--ip')
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()

    print(f'Starting server on {args.ip}:{args.port}')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((args.ip, args.port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f'Connection - {address[0]} : {address[1]} ')

        req = client.recv(1024)
        req = req.decode('utf-8')
        req = HttpRequest(req)
        res = HttpResponse('HTTP/1.1', 404, 'Not Found')
        
        if '/' == req.path:
            client.sendall(bytes(res.text, "utf-8"))
        elif '/helo' == req.path:
            client.sendall(bytes(res.text, "utf-8"))
        else:
            client.sendall(bytes(res.text, 'utf-8'))
        
        client.close()
