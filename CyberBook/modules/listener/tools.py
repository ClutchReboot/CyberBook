import socket
import platform
import datetime


def gather():
    hostname = socket.gethostname()
    return {
        "hostname": hostname,
        "hostByHostname": socket.gethostbyname(hostname),
        "hostByAddress": list(socket.gethostbyname_ex(hostname)),
        "platform": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor()
        },
        "latestUpdate": datetime.datetime.now().strftime('%H%M-%d%m%Y')
    }
