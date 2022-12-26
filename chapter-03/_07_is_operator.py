x = 10
y = 10

print("id x:", id(x)) #id x: 140425382855184 <= memory address
print("id y:", id(y)) #id y: 140425382855184

print("x is y:", x is y) #x is y: True

a = [20, 30, 40]
b = [20, 30, 40]

print("id a:", id(a)) # id a: 139722404126592
print("id b:", id(b)) # id b: 139722404204736

print("a is b:", a is b) # a is b: False