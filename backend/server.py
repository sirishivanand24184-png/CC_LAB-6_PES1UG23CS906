from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        hostname = socket.gethostname()
        body = f"Served by backend: {hostname}\n".encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, format, *args):
        return

server = HTTPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
