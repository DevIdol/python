x = [0, 10, 25, 200]
my_bytes = bytes(x)
print("my_bytes => ", my_bytes)  # my_bytes =>  b'\x00\n\x19\xc8'
# type of my_bytes => <class 'bytes'>
print("type of my_bytes =>", type(my_bytes))
# my_bytes[1] = 444 #TypeError: 'bytes' object does not support item assignment
print("my_bytes[1]=> ", my_bytes[1])  # my_bytes[1]=>  10
