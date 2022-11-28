from CyberBook.listener import SummoningCircle


class CyberBookInterpreter:
    """
    Interactive mode for all of CyberBook.
    """
    def __init__(self):

        self.prompt: str = '[CBI]-$ '
        self.command_prefix: str = '--'

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
        try:
            x = SummoningCircle()
            while True:

                unprocessed_command = input(self.prompt)
                if not unprocessed_command.strip():
                    # empty command or no clients
                    continue

                split_command = unprocessed_command.split()

                print(x.instruction(*split_command))

        except KeyboardInterrupt:
            exit()
