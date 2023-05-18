from concurrent.futures import ThreadPoolExecutor
from http.server import HTTPServer, SimpleHTTPRequestHandler
import time


class QuickHttpServer:
    def __init__(self, ip: str = '', port: int = 8000):
        """
        The HTTP server starts when this class is instantiated.
        This allows users the ability to start an HTTP server for file transfer in the background.
        """
        server_address = (ip, port)

        server_class = HTTPServer
        self.httpd = server_class(server_address, SimpleHTTPRequestHandler)

        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(self.httpd.serve_forever)

    def stop(self):
        self.httpd.shutdown()


if __name__ == '__main__':
    hs = QuickHttpServer()
    time.sleep(5)
    hs.stop()
