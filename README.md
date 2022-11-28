# CyberBook
This is a collection of functions / tools that are used frequently enough to store them some place.
Since most of these will be used in the backend and the backend is sometimes referred to as "magic",
you may notice a theme.

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