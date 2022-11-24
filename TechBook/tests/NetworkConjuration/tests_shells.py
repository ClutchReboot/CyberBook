from TechBook import NetworkConjuration
import socket
# NetworkConjuration.listener(local_host='0.0.0.0', local_port=5000)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 5000))
s.listen(5)
print(input('# '))
while True:
    try:
        client_socket, client_address = s.accept()
        print(f"Connection: {client_address[0]}:{client_address[1]} ")
    except (SystemExit, KeyboardInterrupt):
        if client_socket:
            client_socket.close()
        s.shutdown()
        s.close()
        break
