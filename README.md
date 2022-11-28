# CyberBook
This is a collection of functions / tools that are used frequently enough to store them some place.

## Example
```python
from CyberBook.encoders import DecoderRing
from CyberBook import listener
from CyberBook import wordlists

# CrypticItems
x = DecoderRing(data="test")
x.base64_encode()
print(f"{x.altered_data}")

# NetworkPortals
print(f"{listener.gather()}")

# FileSystemMagic
print(f'{wordlists.read_wordlist(file="someWords.lst")}')
```