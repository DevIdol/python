#Tuple is read only

ages = (18, 20);

print("Ages =>", ages, type(ages)) #Ages => (18, 20) <class 'tuple'>
print("Ages[1] =>", ages[1]) #Ages[1] => 20

# ages[0] = 18;
# print(ages) #TypeError: 'tuple' object does not support item assignment