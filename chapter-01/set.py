my_set = {2, 1, 6}
print("my set =>", my_set, type(my_set))  # my set => {1, 2, 6} <class 'set'>

my_set = set([2, 8, 6])
print("my set =>", my_set)  # my set => {8, 2, 6}

my_set.add(77)
print("my set =>", my_set)  # my set => {8, 2, 77, 6}

my_set.remove(77)
print("my set =>", my_set)  # my set => {8, 2, 6}
