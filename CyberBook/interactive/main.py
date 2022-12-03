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

    def _parser(self, command: str) -> dict:
        """
        Parse used to set up decision-making.
        """

        split_command = command.split()

        parsed_object = {
            "command": split_command[0],
            "options": None,
            "asList": split_command,
            "isCommand": False
        }

        if command.startswith(self.command_prefix):
            parsed_object["isCommand"] = True

        if len(split_command) > 1:
            parsed_object["options"] = split_command[1]

        return parsed_object

    def _set_modules(self, module: str):
        """
        Validate module exists.
        Set self.current_module.
        Update self.prompt.
        """
        if module in self.modules.keys():
            self.current_module = self.modules.get(module)
            self.prompt: str = f'[CBI-{module.upper()}]-$ '
            return f"Module set to '{module}'."
        return f"Module '{module}' not found."

    def _help(self):
        message = f"""
    [*] CyberBookInterpreter
    
    Utilize '{self.command_prefix}' to access parser utilities.
    Otherwise, commands will be sent directly to modules. 
    
        --module {list(self.modules.keys())}
            Select module to use. SummoningCircle on by default.
        --help
            Display help message.
    """

        return message

    def start_interpreter(self):
        try:
            while True:

                results = 'Something may have gone wrong. Check syntax.'

                unprocessed_command = input(self.prompt)
                if not unprocessed_command.strip():
                    # or no clients
                    continue


                split_command = unprocessed_command.split()
                parsed_command = self._parser(command=unprocessed_command)

                if parsed_command.get('command', '').startswith(self.command_prefix):
                    # First sort by self.command_prefix

                    if 'module' in parsed_command['command']:
                        results = self._set_modules(module=parsed_command['options'])
                    elif 'exit' in parsed_command['command']:
                        quit()
                    elif 'help' in parsed_command['command']:
                        results = self._help()

                else:
                    results = self.current_module(*parsed_command['asList'])

                print(results)

        except KeyboardInterrupt:
            exit()
