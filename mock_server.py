from http.server import BaseHTTPRequestHandler, HTTPServer

class MockRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

def start_mock_server():
    server_address = ('localhost', 8050)
    httpd = HTTPServer(server_address, MockRequestHandler)
    print('Mock server running on localhost:8050...')
    httpd.serve_forever()

start_mock_server()
