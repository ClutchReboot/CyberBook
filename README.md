# TechBook (Technomancer's Spellbook)
This is a collection of functions / tools that are used frequently enough to store them some place.
Since most of these will be used in the backend and the backend is sometimes referred to as "magic",
you may notice a theme.

## Example
```python
from TechBook import CrypticItems
from TechBook import NetworkPortals
from TechBook import FileSystemMagic

# CrypticItems
x = CrypticItems.DecoderRing(data="test")
x.base64_encode()
print(f"{x.altered_data}")

# Check NetworkPortals
print(f"{NetworkPortals.gather()}")

# Check FileSystemMagic
print(f'{FileSystemMagic.read_wordlist(file="someWords.lst")}')
```