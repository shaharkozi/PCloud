from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO


class HttpController(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD</h1><body><html>", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        print(response.getvalue())

def run():
    port = 8080
    host = "127.0.0.1"
    server = HTTPServer((host,port), HttpController)
    server.serve_forever()
    server.server_close()

# if __name__ == "__main__":
#     run()
