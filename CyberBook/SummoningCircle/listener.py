import socket
from threading import Thread
from time import sleep


class Server:
    """
    Listener designed to work with Netcat reverse shells.
    """
    def __init__(
            self,
            local_host: str = '0.0.0.0',
            local_port: int = 5000,
    ):

        self.local_host = local_host
        self.local_port = local_port

        self.server: socket = None
        self.active_session: socket = None

        self.active_client_index: int = 0
        self.active_session: socket = None

        self.clients = []
        """
        self.clients = [{
            "client_nickname": str,
            "client_address": str,
            "client_socket": socket
        }]
        """

    def bind_socket(self) -> None:
        """
        Start listening socket server.
        """
        try:

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.local_host, self.local_port))
            self.server.listen(5)

            print(f"Listening for connection(s)...")

            while True:
                client_socket, client_address = self.server.accept()
                self.active_session = client_socket

                # Inherited self.clients from Interpreter
                self.clients.append({
                    "client_nickname": client_address,
                    "client_address": client_address,
                    "client_socket": client_socket
                })

                print(f"Connection: {client_address[0]}:{client_address[1]}")

        except (socket.error, KeyboardInterrupt):
            print(f'[-] Problem encountered: {socket.error} ')
