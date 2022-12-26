num_of_sub = int(input("Enter number of subject: "))
marks = []

pass_mark = 40

for i in range(num_of_sub):
    mark = int(input("Enter mark for subject: " + str(i)+" "))
    marks.append(mark)
print("Mark: ", marks)
