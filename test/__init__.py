import unittest

from httpserver import HttpRequest, HttpResponse


class TestHttpRequest(unittest.TestCase):
    def test_minimalHTTPreq(
        self,
    ):  # METHOD                   PATH                 VERSON
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

        reqDELETE = HttpRequest(
            "DELETE /index.html HTTP/1.0"
        )  # X = class    x its object class ,  class
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
        req = HttpRequest(
            "GET /index.html HTTP/1.0\nContent-Length: 123\n\nHello World"
        )
        self.assertEqual(req.headers["Content-Length"], "123")
        self.assertEqual(req.body, "Hello World")


class TestHTTPResponse(unittest.TestCase):
    def test_HttpResponse404(self):
        response = HttpResponse("HTTP/1.1", 404, "Not Found")
        self.assertEqual(response.text, "HTTP/1.1 404 Not Found")

    def test_Httpresponse200(self):
        response = HttpResponse("HTTP/1.1", 200, "OK")
        self.assertEqual(response.text, "HTTP/1.1 200 OK")

    def test_Httpresponse302(self):
        response = HttpResponse("HTTP/1.1", 302, "Found")
        self.assertEqual(response.text, "HTTP/1.1 302 Found")

    def test_HTTPHeaders(self):
        response = HttpResponse(
            "HTTP/1.1", 404, "Not Found", {"headerA": "valueA", "headerB": "valueB"}
        )
        self.assertEqual(
            response.text,
            "HTTP/1.1 404 Not Found\nheaderA: valueA\nheaderB: valueB\n\n",
        )

    def test_HTTPBody_No_Headers(self):
        response = HttpResponse("HTTP/1.1", 404, "Not Found", None, "Test Body")
        self.assertEqual(
            response.text,
            "HTTP/1.1 404 Not Found\nContent-Length: 9\nContent-Type: text/html; charset=utf-8\n\nTest Body",
        )

    def test_HTTPBodyWithHeaders(self):
        response = HttpResponse(
            "HTTP/1.1",
            404,
            "Not Found",
            {"headerA": "valueA", "headerB": "valueB"},
            "Test Body",
        )
        self.assertEqual(
            response.text,
            "HTTP/1.1 404 Not Found\nheaderA: valueA\nheaderB: valueB\nContent-Length: 9\nContent-Type: text/html; charset=utf-8\n\nTest Body",
        )
