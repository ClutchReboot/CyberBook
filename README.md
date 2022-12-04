# CyberBook
This is a collection of functions / tools that are used frequently enough to store them some place.

## Example

```python
import CyberBook

# CrypticItems
dr = CyberBook.DecoderRing(data="test")
dr.base64_encode()
print(f"{dr.altered_data}")

# NetworkPortals
print(f"{CyberBook.Identify.os_specs()}")

# FileSystemMagic
print(f'{CyberBook.read_wordlist(file="someWords.lst")}')
```