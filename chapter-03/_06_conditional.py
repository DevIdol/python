x = float(input("Enter x: "))
y = float(input("Enter y: "))

max = x if x > y else y # if is an expression, not a statement (like ternary operator)

print("Max:", max)
