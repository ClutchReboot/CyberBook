import socket
from select import select
import threading
from time import sleep

from sys import stdout


class Listener:
    def __init__(self, local_host: str = '0.0.0.0', local_port: int = 5000):
        self.local_host = local_host
        self.local_port = local_port

        self.clients = []

        self.settings = {
            "active_client_session": 0
        }

    def send_command(
            self,
            command,
            buffer_size: int = 1024,
            carriage_return: str = '\n',
            timeout_in_sec: int = 5
    ) -> str:

        active_client_session = self.settings.get('active_client_session')
        client_socket = self.clients[active_client_session].get('client_socket')

        client_socket.send(f"{command}{carriage_return}".encode())

        # Confirm data is being sent with a timeout
        ready = select([client_socket], [], [], timeout_in_sec)

        if ready[0]:
            output = client_socket.recv(buffer_size).decode()
            return output

        return 'Timed Out.'

    def bind_socket(self) -> None:
        try:
            self.clients = []
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.local_host, self.local_port))
            s.listen(5)
            print(f"Incoming Connections:")

            while True:
                client_socket, client_address = s.accept()
                self.clients.append({
                    "client_address": client_address,
                    "client_socket": client_socket
                })

                print(f"Connection: {client_address[0]}:{client_address[1]}")

            # s.shutdown()
            # s.close()

        except (KeyboardInterrupt, socket.error):
            print(f'[-] Problem encountered: {socket.error} ')
            exit()

    def start(self):
        listener = threading.Thread(target=self.bind_socket)
        listener.start()
        sleep(1)

        while True:
            command = input('[NetworkConjuration]-$ ')
            if not command.strip():
                # empty command
                continue

            if command.lower() == "nc exit":
                # if the command is 'np exit', just break out of the loop
                break

            print(f"Sending command: {command}")
            print(self.send_command(command=command))


Listener(local_host='0.0.0.0', local_port=5000).start()
