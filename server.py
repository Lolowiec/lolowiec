import socket


def parse_HTTP(req):
    return "GET"


parse_HTTP("GET")


# if __name__ == "__main__":
#     ip = "127.0.0.1"
#     port= 1235

#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((ip, port))
#     server.listen(5)


#     while True:
#         client, address = server.accept()
#         print(f"Connection - {address[0]} : {address[1]} ")

#         request = client.recv(1024)
#         request = request.decode("utf-8")
#         if 'GET' in request :
#             print('Its GET')
#         if 'POST' in request :
#             print('Its POST')
#         if 'PUT' in request :
#             print('Its PUT')
#         if 'DELETE' in request :
#             print('Its DELETE')

#         print(request)
#         client.close()
