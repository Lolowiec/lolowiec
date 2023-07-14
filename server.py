import unittest


def parse_HTTP(req):
    res = []
    temp = ""
    for x in req:
        print(x)
        if " " in x:
            res.append(temp)
            temp = ""
        else:
            temp += x
    res.append(temp)
    return tuple(res)


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(parse_HTTP("GET /index.html"), ("GET", "/index.html"))
        self.assertEqual(parse_HTTP("POST /index.html"), ("POST", "/index.html"))
        self.assertEqual(parse_HTTP("PUT /index.html"), ("PUT", "/index.html"))
        self.assertEqual(parse_HTTP("DELETE /index.html"), ("DELETE", "/index.html"))


if __name__ == "__main__":
    unittest.main()


# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port= 1235

#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((ip, port))
#     server.listen(5)


#     while True:
#         client, address = server.accept()
#         print(f'Connection - {address[0]} : {address[1]} ')

#         request = client.recv(1024)
#         request = request.decode('utf-8')
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
