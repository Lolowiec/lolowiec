import socket
import unittest


class HttpRequest:
    def __init__(self, req: str): 
        reqlines = req.splitlines()                     #cały tekst 
        firstrow =  reqlines[0].split(' ')              #linia 0
        self.headers = {}
        self.method = firstrow[0]
        self.path = firstrow[1]
        self.verson = firstrow[2]
        self.body = ''
        if '\n\n' in req:
            P = req.find('\n\n')
            self.body = req[P+2:]
        for i in range(1, len(reqlines)) :
            headerrow = reqlines[i]                     #nagłówki
            B = headerrow.find(':')
            key = headerrow[:B]
            value = headerrow[B+1:]
            self.headers[key] = value.strip()
        #zmiena    vartość


class TestHttpRequest(unittest.TestCase):
    def test_minimalHTTPreq(self):                                      # METHOD                   PATH                 VERSON
        reqGET = HttpRequest("GET /index.html HTTP/1.0")
        self.assertEqual(reqGET.method, "GET")
        self.assertEqual(reqGET.path, "/index.html")
        self.assertEqual(reqGET.verson, "HTTP/1.0")

        reqPOST = HttpRequest("POST /index.html HTTP/1.0")
        self.assertEqual(reqPOST.method, "POST")
        self.assertEqual(reqPOST.path, "/index.html")
        self.assertEqual(reqPOST.verson, "HTTP/1.0")

        reqPUT = HttpRequest("PUT /index.html HTTP/1.0")
        self.assertEqual(reqPUT.method, "PUT")
        self.assertEqual(reqPUT.path, "/index.html")
        self.assertEqual(reqPUT.verson, "HTTP/1.0")

        reqDELETE = HttpRequest("DELETE /index.html HTTP/1.0")
        self.assertEqual(reqDELETE.method, "DELETE")
        self.assertEqual(reqDELETE.path, "/index.html")
        self.assertEqual(reqDELETE.verson, "HTTP/1.0")


    def test_HTTPHeders(self):
        req = HttpRequest(
            "GET /index.html HTTP/1.0\nHost:localhost:8000\nUser-Agent: Mozilla/5.0"
        )
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.path, "/index.html")
        self.assertEqual(req.verson, "HTTP/1.0")
        self.assertEqual(req.headers["Host"], "localhost:8000")
        self.assertEqual(req.headers["User-Agent"], "Mozilla/5.0")


        req = HttpRequest(
            "GET /index.html HTTP/1.0\nHost:localhost:8000 \nUser-Agent:  Mozilla/5.0 "
        )
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.path, "/index.html")
        self.assertEqual(req.verson, "HTTP/1.0")
        self.assertEqual(req.headers["Host"], "localhost:8000")
        self.assertEqual(req.headers["User-Agent"], "Mozilla/5.0")
    
    
    def test_HTTPBody(self):
        req = HttpRequest('GET /index.html HTTP/1.0\nContent-Length: 123\n\nHello World')
        self.assertEqual(req.headers['Content-Length'], '123')
        self.assertEqual(req.body,'Hello World')

    



class HttpResponse:
    def __init__(self, verson:str , status_code:int , status_text:str , headers:dict|None = None , body:str|None = None ) -> None:
        self.text =  f'{verson} {status_code} {status_text}'
        if headers is not None:
            self.text += '\n'
            for (key,value) in headers.items() :
                self.text += f'{key}: {value}\n'
            self.text += '\n'
        if body is not None:
            if headers is not None:
                self.text = self.text.removesuffix('\n\n') 
            self.text += f'\nContent-Length: {len(body)}\nContent-Type: text/html; charset=utf-8\n\n{body}'

        

class TestHTTPResponse(unittest.TestCase):
    def test_HttpResponse404(self):
        response = HttpResponse('HTTP/1.1', 404, 'Not Found')
        self.assertEqual(response.text, 'HTTP/1.1 404 Not Found')
        

    def test_Httpresponse200(self):
        response = HttpResponse('HTTP/1.1' ,200, 'OK')
        self.assertEqual(response.text, 'HTTP/1.1 200 OK')
        

    def test_Httpresponse302(self):
        response = HttpResponse('HTTP/1.1' ,302, 'Found')
        self.assertEqual(response.text, 'HTTP/1.1 302 Found')


    def test_HTTPHeaders(self):
        response = HttpResponse('HTTP/1.1' ,404, 'Not Found', {'headerA': 'valueA' , 'headerB': "valueB"})
        self.assertEqual(response.text, 'HTTP/1.1 404 Not Found\nheaderA: valueA\nheaderB: valueB\n\n')


    def test_HTTPBody_No_Headers(self):
        response = HttpResponse('HTTP/1.1' ,404, 'Not Found', None , 'Test Body')
        self.assertEqual(response.text, 'HTTP/1.1 404 Not Found\nContent-Length: 9\nContent-Type: text/html; charset=utf-8\n\nTest Body')


    def test_HTTPBodyWithHeaders(self):
        response = HttpResponse('HTTP/1.1' ,404, 'Not Found', {'headerA': 'valueA' , 'headerB': "valueB"} , 'Test Body')
        self.assertEqual(response.text, 'HTTP/1.1 404 Not Found\nheaderA: valueA\nheaderB: valueB\nContent-Length: 9\nContent-Type: text/html; charset=utf-8\n\nTest Body')





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

#         req = client.recv(1024)
#         req = req.decode('utf-8')
#         req = HttpRequest(req)

        
#         if '/' == req.path:
#             client.sendall(bytes('htlm', "utf-8"))
#         elif '/haelo' == req.path:
#             client.sendall(bytes('Hello World', "utf-8"))
#         else:
#             client.sendall(bytes('HTTP/1.1 404 Not Found', 'utf-8'))
        
#         client.close()
    






