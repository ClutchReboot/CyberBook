from CyberBook import modules


class CyberBookInterpreter:
    """
    Interactive mode for all of CyberBook.
    """
    def __init__(self):

        self.prompt: str = '[CBI]-$ '
        self.command_prefix: str = '--'

        self.sc = modules.SummoningCircle()
        self.dr = modules.DecoderRing(data='')

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

        if parsed_object["command"].startswith(self.command_prefix):
            parsed_object["isCommand"] = True

        if len(split_command) > 1:
            parsed_object["options"] = split_command[1:]

        return parsed_object

    def _set_modules(self, module: str):
        """
        Validate module exists.
        Set self.current_module.
        Update self.prompt.
        """
        print(
            f"module: {module}",
            f"keys: {self.modules.keys()}",
            sep='\n'
        )
        if module in self.modules.keys():
            self.current_module = self.modules.get(module)
            self.prompt: str = f'[CBI-{module.upper()}]-$ '
            return f"Module set to '{module}'."
        return f"Module '{module}' not found."

    def _help(self):
        message = f"""
    [*] CyberBookInterpreter
    
    Utilize '{self.command_prefix}' to access Interpreter utilities.
    Otherwise, commands will be sent directly to modules. 
    
        {self.command_prefix}module {list(self.modules.keys())}
            Select module to use. SummoningCircle on by default.
        {self.command_prefix}exit
            Exit Interactive mode.
        {self.command_prefix}help
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

                parsed_command = self._parser(command=unprocessed_command)

                if parsed_command['isCommand']:
                    # First sort by self.command_prefix

                    if 'module' in parsed_command['command']:
                        results = self._set_modules(*parsed_command['options'])
                    elif 'exit' in parsed_command['command']:
                        quit()
                    elif 'help' in parsed_command['command']:
                        results = self._help()

                else:
                    results = self.current_module(*parsed_command['asList'])

                print(results)

        except KeyboardInterrupt:
            exit()
