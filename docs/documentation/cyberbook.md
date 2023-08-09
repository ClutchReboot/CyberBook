## Purpose
This is a collection of functions / tools that are used frequently enough to store them some place.

### DecoderRing Example
The purpose of DecoderRing is to encode / decode a string easily.
```python
import CyberBook

# DecoderRing Usage
dr = CyberBook.DecoderRing

print(
    # Encode using Hex
    f"Hex encoded: \t\t{dr.basic_hex(data='test')}",

    # Encode using Base64
    f"Base64 encoded: \t{dr.base64(data='test')}",

    # Decode Base64
    f"Base64 decoded: \t{dr.base64(data='NzQ2NTczNzQ=', decode=True)}",

    # Decode Hex
    f"Hex decoded: \t\t{dr.basic_hex(data='74657374', decode=True)}",
    sep='\n'
)
```
Expected Output:
```commandline
Hex encoded: 		74657374
Base64 encoded: 	dGVzdA==
Base64 decoded: 	74657374
Hex decoded: 		test
```

### Summon Circle Example
This is mainly used as a Listener for reverse shells or a quick way to automate TCP responses.
The following is a Listener that should work with a netcat reverse shell.
```python
import CyberBook


sc = CyberBook.SummoningCircle()
sc.start()

while sc.server:
    command = input("~$ ")
    if command == 'exit':
        sc.close()
    else:
        sc.send_recv(data=command)
```
By default, the listener will listen to any IP on the host system and port 5000.