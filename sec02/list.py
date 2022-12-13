countries = ["Myanmar", "Thailand", "Myalaysia", "Singapore", 2, True]

print(countries) #['Myanmar', 'Thailand', 'Myalaysia', 'Singapore', 2, True]
print(countries[1]) #Thailand
print(countries[-2]) #Myalaysia
print(countries[1][2]) #[1] => Thailand / [2] => a
print(countries[3:]) #["Singapore"]
print(countries[2:3]) #["Myalaysia"]
print(countries[1:3]) #["Thailand", "Myalaysia"]
print(len(countries)) #4
print(type(countries)) #<class 'list'>
print(type(countries[5]))#<class 'bool'>

countries2 = list(("Myanmar", "Thailand", "Myalaysia", "Singapore", 2, True))
print(countries2)