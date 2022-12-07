# CyberBook
This is a collection of functions / tools that are used frequently enough to store them some place.

## DecoderRing Example
The purpose of DecoderRing is to encode / decode a string easily.
```python
import CyberBook

# DecoderRing Usage
dr = CyberBook.DecoderRing(data='test')

print(
    "[*] Encode:\n",
    f"Hex encoded: \t\t{dr.hex()}",
    f"Base64 encoded: \t{dr.base64()}",
    "\n[*] Accessing Data:\n",
    f"Initial input: \t\t{dr.data}",
    f"Encrypted string: \t{dr.altered_data}",
    "\n[*] Decode:\n",
    f"Base64 decoded: \t{dr.base64(decode=True)}",
    f"Hex decoded: \t\t{dr.hex(decode=True)}",
    sep='\n'
)
```
Expected Output:
```commandline
[*] Encode:

Hex encoded: 		74657374
Base64 encoded: 	NzQ2NTczNzQ=

[*] Accessing Data:

Initial input: 		test
Encrypted string: 	NzQ2NTczNzQ=

[*] Decode:

Base64 decoded: 	74657374
Hex decoded: 		test
```

## Other Module Examples
```python
# Identify
print(f"{CyberBook.Identify.os_specs()}")

# FileSystemMagic
print(f'{CyberBook.read_wordlist(file="someWords.lst")}')

```