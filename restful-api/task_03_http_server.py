#!/usr/bin/python3
"""
    Function file for Server http.server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Handle GET requests. """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_error(404, "Endpoint not found")


if __name__ == "__main__":
    HOSTNAME = ""
    PORT = 8000
    server = HTTPServer((HOSTNAME, PORT), Server)
    print(f'Server started at port {PORT}...')
    server.serve_forever()