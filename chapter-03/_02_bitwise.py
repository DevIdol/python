x = 2
y = 3

print('bin(2):', bin(x)) #bin(2): 0b10
print('bin(3):', bin(y)) #bin(3): 0b11
print("bin(2) & bin(3):", x & y) #bin(2) & bin(3): 2

def getTrue():
    print("Get True")
    return True
def getFalse():
    print ("Get False")
    return False

print("getTrue() & getFalse():", getTrue() & getFalse())
# Get True
# Get False
# getTrue() & getFalse(): False

print("getTrue() | getFalse():", getTrue() | getFalse())
# Get True
# Get False
# getTrue() | getFalse(): False