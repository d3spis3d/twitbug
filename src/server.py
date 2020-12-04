import json
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

from . import scraper

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def _write_json(self, content):
        return json.dumps(content).encode("utf8")

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._write_json(scraper.tweet_store.get_tweets()))

    def log_message(self, format, *args):
        return

class Server(Thread):
    def __init__(self, address, port):
        Thread.__init__(self)
        self.address = address
        self.port = port

    def run(self):
        server_address = (self.address, self.port)
        httpd = HTTPServer(server_address, Handler)

        print(f"Running twitbug server on {self.address}:{self.port}, GET / for fetched tweets\n")

        httpd.serve_forever()