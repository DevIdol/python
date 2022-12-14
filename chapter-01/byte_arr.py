x = [0, 10, 25, 200]
my_bytes = bytearray(x)

my_bytes[1] = 20

print("my_bytes =>", my_bytes)  # my_bytes => bytearray(b'\x00\x14\x19\xc8')
print("my_bytes[1] =>", my_bytes[1])  # my_bytes[1] => 20
