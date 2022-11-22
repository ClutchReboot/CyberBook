from TechBook.EncoderDecoderRing import EncoderDecoderRing
import NetworkPortals


x = EncoderDecoderRing(data="test")
x.base64_encode()
print(f"{x.altered_data=}")

# Check NetworkPortals
print(f"{NetworkPortals.gather()}")
NetworkPortals.listener(local_host='127.0.0.1', local_port=5000)


