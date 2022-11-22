import CrypticItems
import NetworkPortals
import FileSystemMagic

# CrypticItems
x = CrypticItems.DecoderRing(data="test")
x.base64_encode()
print(f"{x.altered_data=}")

# Check NetworkPortals
print(f"{NetworkPortals.gather()}")
NetworkPortals.listener(local_host='127.0.0.1', local_port=5000)

# Check FileSystemMagic
print(f'{FileSystemMagic.read_wordlist(file="somethingAwesome.txt")}')
