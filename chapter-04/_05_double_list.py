my_list = [10, 20, 30, 40]

for i in my_list:
    print("i is:", i)
    i *= 2  # it doesn't work

print("My List:", my_list)  # My List: [10, 20, 30, 40]

for i in range(len(my_list)):
    print("My List Item:", my_list[i])
    my_list[i] = my_list[i] * 2  # it works

print("My List:", my_list)  # My List: [20, 40, 60, 80]
