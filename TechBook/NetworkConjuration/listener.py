import socket
from threading import Thread
from time import sleep

from .interpreter import Interpreter


class SummoningCircle(Interpreter):
    """
    Listener designed to work with Netcat reverse shells.
    """
    def __init__(
            self,
            local_host: str = '0.0.0.0',
            local_port: int = 5000,
            command_prefix: str = '-sc',
            timeout_in_sec: int = 5
    ):

        super().__init__()

        self.local_host = local_host
        self.local_port = local_port
        self.command_prefix = command_prefix

        # Designed to be user settings down the road
        self.carriage_return: str = '\n'
        self.timeout_in_sec = timeout_in_sec

        self.server: socket = None
        self.active_session: socket = None
        self.clients = []

    def bind_socket(self) -> None:
        try:

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.local_host, self.local_port))
            self.server.listen(5)

            print(f"Listening for connection(s)...")

            while True:
                client_socket, client_address = self.server.accept()
                self.active_session = client_socket
                self.clients.append({
                    "client_nickname": client_address,
                    "client_address": client_address,
                    "client_socket": client_socket
                })

                print(f"Connection: {client_address[0]}:{client_address[1]}")

        except (socket.error, KeyboardInterrupt):
            print(f'[-] Problem encountered: {socket.error} ')

    def start(self):
        listener = Thread(target=self.bind_socket)
        listener.start()
        sleep(1)
        self.start_interpreter()


if __name__ == '__main__':
    SummoningCircle().start()
