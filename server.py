import http.server
import socketserver
import json
import os
import socket
import urllib.parse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'lessons')
os.makedirs(DATA_DIR, exist_ok=True)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/ip':
            ip = get_local_ip()
            data = json.dumps({'ip': ip, 'port': PORT}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(data)
            return

        if parsed.path == '/api/get-lesson':
            qs = urllib.parse.parse_qs(parsed.query)
            lesson_id = qs.get('id', [''])[0]
            # Sanitize filename
            clean_id = ''.join(c for c in lesson_id if c.isalnum() or c in '-_')
            file_path = os.path.join(DATA_DIR, f"{clean_id}.json")
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(content)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_response(404)
                self.end_headers()
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/save-lesson':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                lesson_id = str(data.get('id', ''))
                clean_id = ''.join(c for c in lesson_id if c.isalnum() or c in '-_')
                if not clean_id:
                    clean_id = f"lesson_{int(os.times()[4])}"
                
                file_path = os.path.join(DATA_DIR, f"{clean_id}.json")
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f)

                resp = json.dumps({'status': 'ok', 'id': clean_id}).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(resp)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp)
            except Exception as e:
                err = json.dumps({'error': str(e)}).encode('utf-8')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(err)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(err)
            return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    local_ip = get_local_ip()
    print(f"Server starting on http://{local_ip}:{PORT} and http://localhost:{PORT}")
    with socketserver.TCPServer(('', PORT), CustomHandler) as httpd:
        httpd.serve_forever()
