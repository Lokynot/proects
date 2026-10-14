from http.server import BaseHTTPRequestHandler, HTTPServer

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Project 02 - Jenkins CI/CD Success!")

server = HTTPServer(("0.0.0.0", 8000), App)
print("Project 02 running on port 8000", flush=True)
server.serve_forever()
