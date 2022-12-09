import socket
from threading import Thread
from select import select
from time import sleep


class SummoningCircle:
    """
    Listener designed to work with Netcat reverse shells.
    """
    def __init__(
            self,
            local_host: str = '0.0.0.0',
            local_port: int = 5000,
            timeout_in_sec: int = 5,
            carriage_return: str = '\n'
    ):

        self.local_host = local_host
        self.local_port = local_port
        self.timeout_in_sec = timeout_in_sec
        self.carriage_return = carriage_return

        self.buffer_size = 1024 * 25
        self.max_clients = 5

        self.server: socket = None
        self.clients: list[socket] = []

        self.active_session: socket = None

    def _bind_socket(self) -> None:
        """
        Start listening socket server.
        """
        try:

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.local_host, self.local_port))
            self.server.listen(self.max_clients)

            print(f"Listening for connection(s)...")

            while True:
                client_socket, client_address = self.server.accept()
                self.clients.append(client_socket)

                if not self.active_session:
                    self.active_session = client_socket

                print(f"Connection: {client_address[0]}:{client_address[1]}")

        except (socket.error, KeyboardInterrupt):
            return f'[-] Problem encountered: {socket.error} '

    def end_client_session(self, client_session: socket = None, timer: int = 1):
        """
        Exit client connection and close connection.
        Also, clean up 'self.clients' list.
        """

        if timer:
            sleep(timer)

        if not client_session:
            client_session = self.active_session

        try:
            self.clients.remove(client_session)
            self.active_session = None
            client_session.shutdown(socket.SHUT_RDWR)
            client_session.close()
        except (socket.error, OSError, ValueError):
            pass

    def send(self, data: str, client_session: socket = None) -> str:
        """
        Default way to send data to the active connection's shell.
        """

        if not client_session:
            client_session = self.active_session

        client_session.send(f"{data}{self.carriage_return}".encode())

        return 'Sent.'

    def send_recv(self, data: str, client_session: socket = None) -> str:
        """
        Default way to send data to the active connection's shell.
        """

        if not client_session:
            client_session = self.active_session

        client_session.send(f"{data}{self.carriage_return}".encode())

        # Confirm data is being sent with a timeout
        ready = select([client_session], [], [], self.timeout_in_sec)

        if ready[0]:
            return client_session.recv(self.buffer_size).decode()

        return 'Send / receive timed Out.'

    def start(self):
        """
        Startup SummoningCircle in the background.
        Start interpreter.
        """
        listener = Thread(target=self._bind_socket)
        listener.start()
        return "Server started"

    def stop(self):
        """
        Close client connections and shutdown server.
        """
        try:
            for client in self.clients:
                client.close()
            self.server.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass
        self.server.close()

    def receive(self, client_session: socket = None) -> str:
        """
        Default way to receive data.
        """

        if not client_session:
            client_session = self.active_session

        # Confirm data is being sent with a timeout
        ready = select([client_session], [], [], self.timeout_in_sec)

        if ready[0]:
            return client_session.recv(self.buffer_size).decode()

        return 'Receive timed out.'
