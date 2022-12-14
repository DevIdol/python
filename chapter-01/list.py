ages = [16, 18, 20, 22, 24]

print("Ages =>", ages)  # Ages => [16, 18, 20, 22, 24]

print("Ages[2] =>", ages[2])  # Ages => 20

print("Ages[2] =>", ages[2:4])  # Ages[2] => [20, 22]

print("Average Age =>", sum(ages) / len(ages))  # Average Age => 20.0

ages.append(40)
print('Ages =>', ages)  # Ages => [16, 18, 20, 22, 24, 40]

ages.remove(40)
print('Ages =>', ages)  # Ages => [16, 18, 20, 22, 24]
