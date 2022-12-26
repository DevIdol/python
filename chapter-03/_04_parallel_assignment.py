x = 1
y = 2

temp = x
x = y
y = temp

print("x is:", x)  # x is: 2
print("y is:", y)  # y is: 1

x, y = y, x

print("x is:", x)  # x is: 1
print("y is:", y)  # y is: 2