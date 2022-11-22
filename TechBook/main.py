import CrypticItems
import NetworkPortals
import FileSystemMagic

# CrypticItems
x = CrypticItems.DecoderRing(data="test")
x.base64_encode()
print(f"[*] Encoded: {x.altered_data}")

# Check NetworkPortals
print(f"[*] Gathered Info: {NetworkPortals.gather()}")

# Check FileSystemMagic
print(f'[*] WordList: {FileSystemMagic.read_wordlist(file="FileSystemMagic/basic.lst")}')
