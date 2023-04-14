import socket
import platform
import netifaces


def get_private_ips():
    interfaces = netifaces.interfaces()

    local_ipv4 = dict()
    for interface in interfaces:

        ipv4_info = netifaces.ifaddresses(interface).get(2)
        ipv4_addr = ipv4_info[0].get('addr')
        local_ipv4[interface] = ipv4_addr

    return local_ipv4


def os_specs():
    hostname = socket.gethostname()

    return {
        "hostname": hostname,
        "hostByHostname": socket.gethostbyname(hostname),
        "hostByAddress": list(socket.gethostbyname_ex(hostname)),
        "localIpV4": get_private_ips(),
        "platform": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    }
