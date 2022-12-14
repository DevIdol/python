x = 10
y = 20
z = 10

print("Id of x => ", id(x))  # Id of x =>  139812964139536(Note: Random)
print("Id of y => ", id(y))  # Id of y =>  139812964139856(Note: Random)
print("Id of z => ", id(z))  # Id of z =>  139812964139536(Note: Random)

print("x is y =>", x is y)  # x is y => False
print("x is z =>", x is z)  # x is z => True
