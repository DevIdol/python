x = [10, 20, 30]
i = 0

i, x[i] = 1, 40

print("i:", i)  # i: 2
print("x[i]:", x[i])  # x[i]: 40
print("x:", x)  # x[i]: [10, 40, 40]


def getTwo():
    return (10, 20)


x, y = getTwo()
print("x is:", x, ", y is:", y)  # x is: 10 , y is: 20
