my_str = "123"
my_num = 10

#print("my_str + my_num=>", my_str + my_num)
# TypeError: can only concatenate str (not "int") to str

# int(my_str) + my_num=> 133
print("int(my_str) + my_num=>", int(my_str) + my_num)

print("int(True)=> ", int(True))  # int(True)=>  1
print("int(False)=> ", int(False))  # int(False)=>  0

print("float(True)=> ", float(True))  # float(True)=>  1.0
print("float(False)=> ", float(False))  # float(False)=>  0.0

print("bool(1) => ", bool(1))  # bool(1) =>  True
print("bool(1.0) => ", bool(1.0))  # bool(1.0) =>  True
print("bool(0) => ", bool(0))  # bool(0) =>  False
print("bool(0.0) => ", bool(0.0))  # bool(0.0) =>  False

print("bool('False')=> ", bool('False'))  # bool('False')=>  True

# False => False
# 0 => False
# "" => False
# [] => False
# () => False
