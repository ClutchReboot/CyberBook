from EncoderDecoderRing import EDR

x = EDR(data="test")
x.base64_encode()
print(f"{x.altered_data=}")
