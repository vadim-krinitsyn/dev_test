from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Backend running on http://{HOST}:{PORT}")
    server.serve_forever()