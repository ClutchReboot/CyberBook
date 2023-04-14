import socket
import platform


def get_private_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('1.1.1.2', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'

    finally:
        s.close()
    
    return ip
    
    
def os_specs():
    hostname = socket.gethostname()

    return {
        "hostname": hostname,
        "hostByHostname": socket.gethostbyname(hostname),
        "hostByAddress": list(socket.gethostbyname_ex(hostname)),
        "privateIp": get_private_ip(),
        "platform": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    }
