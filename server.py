import unittest



   


class HTTPreq:
    def __init__(self, req: str): 
        reqlines = req.splitlines()                     #cały tekst 
        firstrow =  reqlines[0].split(' ')              #linia 0
        self.headers = {}
        self.method = firstrow[0]
        self.path = firstrow[1]
        self.verson = firstrow[2]
        for i in range(1, len(reqlines)) :
            headerrow = reqlines[i]                     #nagłówki
            B = headerrow.find(':')
            key = headerrow[:B]
            value = headerrow[B+1:]
            self.headers[key] = value.strip()
            

 
        #zmiena    vartość

            
        
        


class TestStringMethods(unittest.TestCase):
    def test_minimalHTTPreq(self):                                      # METHOD                   PATH                 VERSON
        reqGET = HTTPreq("GET /index.html HTTP/1.0")
        self.assertEqual(reqGET.method, "GET")
        self.assertEqual(reqGET.path, "/index.html")
        self.assertEqual(reqGET.verson, "HTTP/1.0")

        reqPOST = HTTPreq("POST /index.html HTTP/1.0")
        self.assertEqual(reqPOST.method, "POST")
        self.assertEqual(reqPOST.path, "/index.html")
        self.assertEqual(reqPOST.verson, "HTTP/1.0")

        reqPUT = HTTPreq("PUT /index.html HTTP/1.0")
        self.assertEqual(reqPUT.method, "PUT")
        self.assertEqual(reqPUT.path, "/index.html")
        self.assertEqual(reqPUT.verson, "HTTP/1.0")

        reqDELETE = HTTPreq("DELETE /index.html HTTP/1.0")
        self.assertEqual(reqDELETE.method, "DELETE")
        self.assertEqual(reqDELETE.path, "/index.html")
        self.assertEqual(reqDELETE.verson, "HTTP/1.0")

    def test_HTTPHeders(self):
        req = HTTPreq(
            "GET /index.html HTTP/1.0\nHost:localhost:8000\nUser-Agent: Mozilla/5.0"
        )
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.path, "/index.html")
        self.assertEqual(req.verson, "HTTP/1.0")
        self.assertEqual(req.headers["Host"], "localhost:8000")
        self.assertEqual(req.headers["User-Agent"], "Mozilla/5.0")


        req = HTTPreq(
            "GET /index.html HTTP/1.0\nHost:localhost:8000 \nUser-Agent:  Mozilla/5.0 "
        )
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.path, "/index.html")
        self.assertEqual(req.verson, "HTTP/1.0")
        self.assertEqual(req.headers["Host"], "localhost:8000")
        self.assertEqual(req.headers["User-Agent"], "Mozilla/5.0")
        



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






#Host: localhost:8000
# key:Host 
# Value: localhost:8000 