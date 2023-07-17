import unittest


def parse_HTTP(req: str) -> tuple:
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


class HTTPreq:
    def __init__(self, req: str):
        pol = parse_HTTP(req)
        if len(pol) != 3:
            raise ValueError("inwalid HTTP req size")

        self.req = req
        self.method = pol[0]
        self.verson = pol[2]
        self.path = pol[1]


p1 = HTTPreq("GET /index.html HTTP/1.0")


class TestStringMethods(unittest.TestCase):
    def test_minimalHTTPreq(self):  # metod       ścieszka   wersja
        self.assertEqual(
            parse_HTTP("GET /index.html HTTP/1.0"), ("GET", "/index.html", "HTTP/1.0")
        )
        self.assertEqual(
            parse_HTTP("POST /index.html HTTP/1.0"), ("POST", "/index.html", "HTTP/1.0")
        )
        self.assertEqual(
            parse_HTTP("PUT /index.html HTTP/1.0"), ("PUT", "/index.html", "HTTP/1.0")
        )
        self.assertEqual(
            parse_HTTP("DELETE /index.html HTTP/1.0"),
            ("DELETE", "/index.html", "HTTP/1.0"),
        )

    def test_HTTPHeders(self):
        req = HTTPreq(
            "GET /index.html HTTP/1.0\nHost: localhost:8000\nUser-Agent: Mozilla/5.0"
        )
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.path, "/index.html")
        self.assertEqual(req.verson, "HTTP/1.0")


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
