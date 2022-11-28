import socket
from select import select


class CyberBookInterpreter:
    """
    Interactive mode for all of CyberBook.
    """
    def __init__(self):

        self.prompt: str = '[CBI]-$ '
        self.command_prefix: str = '--'

        self._basic_functions = {
            f"{self.command_prefix}shutdown": self.shutdown,
            f"{self.command_prefix}exit": self.exit,
            f"{self.command_prefix}view": self.view_clients
        }

    def _parser(self, command: str) -> list:
        """
        Parse used to set up decision-making.
        """
        if not command.startswith(self.command_prefix):
            # Is not a parser command
            return [None, None]

        split_command = command.split()

        if len(split_command) > 1:
            return [split_command[0], split_command[1:]]
        return [split_command[0], None]

    def start_interpreter(self):
        while True:

            unprocessed_command = input('[SC]-$ ')
            if not unprocessed_command.strip() or not self.clients:
                # empty command or no clients
                continue

            interpreter_command, interpreter_options = self._parser(command=unprocessed_command)

            if interpreter_command in self._basic_functions.keys():
                function = self._basic_functions.get(interpreter_command)
                print(function())
            elif interpreter_command in self._advanced_functions.keys():
                function = self._advanced_functions.get(interpreter_command)
                print(function(interpreter_options))
            else:
                print(self.send_command(command=unprocessed_command))
