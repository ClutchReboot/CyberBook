import socket
from select import select


class Interpreter:
    """
    Interpreter used for SummoningCircle listener.
    """
    def __init__(self):
        self.command_prefix: str = '-sc'

        # Designed to be user settings down the road
        self.buffer_size: int = 1024
        self.carriage_return: str = '\n'
        self.timeout_in_sec: int = 5

        self.server: socket = None
        self.active_session: socket = None
        self.clients = []

    def shutdown(self):
        try:
            for client in self.clients:
                client['client_socket'].close()
            self.server.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass
        self.server.close()
        exit()

    def exit(self):
        try:
            # Create new list excluding current client_socket
            self.clients = [
                client for index, client in enumerate(self.clients) if self.active_session != client['client_socket']
            ]

            self.active_session.shutdown(socket.SHUT_RDWR)
            self.active_session.close()
        except (socket.error, OSError, ValueError):
            pass

    def is_active(self):
        try:
            self.active_session.send(b'echo ping\n')
            return True
        except socket.error:
            return False

    def view_clients(self):
        output = '[*] Summoned Connections\n\n'
        for index, client in enumerate(self.clients):
            output += f"{index} -> {client['client_nickname']} : {client['client_address']}\n"
        return output

    def change_nickname(self, command: str):
        split_command = command.split()
        if len(split_command) > 3:
            index = int(split_command[2])
            name_change = split_command[3]
            self.clients[index]['client_nickname'] = name_change
            return f'Name changed: {name_change}'

    def send_command(self, command: str) -> str:
        self.active_session.send(f"{command}{self.carriage_return}".encode())

        # Confirm data is being sent with a timeout
        ready = select([self.active_session], [], [], self.timeout_in_sec)

        if ready[0]:
            return self.active_session.recv(self.buffer_size).decode()

        return 'Response timed Out.'

    def parser(self, command: str):
        if not command.startswith(self.command_prefix):
            return False

        split_command = command.split()
        if len(split_command) > 1:
            return ' '.join(split_command[:2])

    def start_interpreter(self):
        basic_functions = {
            f"{self.command_prefix} shutdown": self.shutdown,
            f"{self.command_prefix} exit": self.exit,
            f"{self.command_prefix} view": self.view_clients
        }

        advanced_functions = {
            f"{self.command_prefix} name": self.change_nickname
        }

        while True:
            command = input('[SC]-$ ')
            if not command.strip() or not self.clients:
                # empty command or no clients
                continue

            parsed = self.parser(command=command)

            if parsed in basic_functions.keys():
                function = basic_functions.get(parsed)
                print(function())
            elif parsed in advanced_functions.keys():
                function = advanced_functions.get(parsed)
                print(function(command))
            else:
                print(self.send_command(command=command))
