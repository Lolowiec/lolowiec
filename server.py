import socket

from .httpserver import HttpRequest, HttpResponse

if __name__ == '__main__':
    ip = '127.0.0.1'    
    port= 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
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
