num_of_sub = int(input("Enter number of subject: "))
marks = []

pass_mark = 40
isPass = True

for i in range(num_of_sub):
    mark = int(input("Enter mark for subject: " + str(i)+" "))
    marks.append(mark)
    isPass = isPass and mark >= pass_mark
print("Marks: ", marks)
print("Total Mark: ", sum(marks))


if isPass:
    print("Pass the exam")
else:
    print("Fail the exam")
