#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            print(self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.wfile.write(b"Hello, this is a simple API")

        elif self.path == '/data':
            data = {"name": "John",
                    "age": 30,
                    "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd server on port {}'.format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    run()
