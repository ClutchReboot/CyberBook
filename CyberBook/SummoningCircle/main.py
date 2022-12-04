import socket
from select import select
from threading import Thread

from .listener import Server


class SummoningCircle(Server):
    """
    NOTE: Currently, only works with SummoingCircleInterpreter. Separate package.
    Interpreter used for SummoningCircleServer SummoningCircle.
    """
    def __init__(self):

        super().__init__()

        self.command_prefix: str = '--'
        self.buffer_size: int = 1024 * 25
        self.carriage_return: str = '\n'
        self.timeout_in_sec: int = 5

        self._basic_functions = {
            f"{self.command_prefix}shutdown": self.shutdown,
            f"{self.command_prefix}exit": self.exit,
            f"{self.command_prefix}view": self.view_clients
        }

        self._advanced_functions = {
            f"{self.command_prefix}name": self.change_nickname,
            f"{self.command_prefix}session": self.change_session
        }

    def _parser(self, *args, **kwargs) -> list:
        """
        Parse used to set up decision-making.
        """

        args_list = list(args)
        command = args_list.pop(0)

        if len(args) > 1:
            return [command, args_list]
        return [command, None]

    def _set_active_session(self):
        """
        Used to ensure 'self.active_session' is using the correct client socket.
        """
        if self.clients:
            self.active_session = self.clients[self.active_client_index].get('client_socket')

    def change_nickname(self, interpreter_options: list[int, str]):
        """
        Command: Change 'client_nickname' for a specified index in 'self.clients'
        """
        if len(interpreter_options) > 1:
            index = int(interpreter_options[0])
            name_change = interpreter_options[1]
            self.clients[index]['client_nickname'] = name_change
            return f'Name changed: {name_change}'

    def change_session(self, interpreter_options: list[int]):
        """
        Command: Change client session
        """

        self.active_client_index = int(interpreter_options[0])
        return f'Session changed: {self.active_client_index}'

    def exit(self):
        """
        Command: Exit client connection and close connection.
        Also, clean up 'self.clients' list.
        """
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
        """
        Command: Basic ping check to test if client is active.
        Works for basic connections but not a viable solution for shell / SummoningCircle concept.
        """
        try:
            self.active_session.send(b'echo ping\n')
            return True
        except socket.error:
            return False

    def send_command(self, command: str) -> str:
        """
        Command: Default way to send OS commands to the active connection's shell.
        """
        self.active_session.send(f"{command}{self.carriage_return}".encode())

        # Confirm data is being sent with a timeout
        ready = select([self.active_session], [], [], self.timeout_in_sec)

        if ready[0]:
            return self.active_session.recv(self.buffer_size).decode()

        return 'Response timed Out.'

    def shutdown(self):
        """
        Command: Close client connections and shutdown server.
        Finally, system exit.
        """
        try:
            for client in self.clients:
                client['client_socket'].close()
            self.server.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass
        self.server.close()
        exit()

    def start_listener(self):
        """
        Startup SummoningCircle in the background.
        Start interpreter.
        """
        listener = Thread(target=self.bind_socket)
        listener.start()
        return "Server started"

    def view_clients(self):
        """
        Command: View all client connections in 'self.clients'
        """
        output = '[*] Summoned Connections\n\n'
        for index, client in enumerate(self.clients):
            output += f"{index} -> {client['client_nickname']} : {client['client_address']}\n"
        return output

    def instruction(self, *args, **kwargs):
        """
        Used for decision making. Called by main interpreter function.
        """

        if 'start' == args[0].lower():
            return self.start_listener()

        if not self.clients:
            # empty command or no clients
            return "No clients"

        self._set_active_session()

        interpreter_command, interpreter_options = self._parser(*args, **kwargs)

        if interpreter_command in self._basic_functions.keys():
            function = self._basic_functions.get(interpreter_command)
            print(function())
        elif interpreter_command in self._advanced_functions.keys():
            function = self._advanced_functions.get(interpreter_command)
            print(function(interpreter_options))
        else:
            command = ' '. join(list(args))
            print(self.send_command(command=command))
