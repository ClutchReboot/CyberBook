from enum import Enum

from CyberBook.encoders import DecoderRing
from CyberBook.listener import SummoningCircle


class CyberBookInterpreter:
    """
    Interactive mode for all of CyberBook.
    """
    def __init__(self):

        self.prompt: str = '[CBI]-$ '
        self.command_prefix: str = '--'

        self.sc = SummoningCircle()
        self.dr = DecoderRing(data='')

        self.current_module = self.sc.instruction

        self.modules = {
            'summoning_circle': self.sc.instruction,
            'sc': self.sc.instruction
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

    def _set_modules(self, module: str):
        if module in self.modules.keys():
            self.current_module = self.modules.get(module)
            self.prompt: str = f'[CBI-{module.upper()}]-$ '
            return f"Module set to '{module}'."
        return f"Module '{module}' not found."

    def start_interpreter(self):
        try:
            while True:

                unprocessed_command = input(self.prompt)
                if not unprocessed_command.strip():
                    # or no clients
                    continue
                elif 'exit' == unprocessed_command.lower():
                    quit()

                split_command = unprocessed_command.split()

                if split_command[0] == '--module' and split_command[1].lower() in self.modules.keys():
                    print(self._set_modules(module=split_command[1]))
                else:
                    print(self.current_module(*split_command))

        except KeyboardInterrupt:
            exit()
