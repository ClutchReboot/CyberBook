from TechBook.EncoderDecoderRing import EncoderDecoderRing
import NetworkPortals


x = EncoderDecoderRing(data="test")
x.base64_encode()
print(f"{x.altered_data=}")

# Check NetworkPortals
print(f"{NetworkPortals.gather()}")
NetworkPortals.listener(local_host='192.168.0.126', local_port=5000)


