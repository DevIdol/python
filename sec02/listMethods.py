list1 = [1, 2, 3];
list2 = ["Banana", "Orange", "Cherry"]
list3 = [5, 6, 2, 8, 3, 9, 1, 4, 7]

list1.extend(list2);
print(list1); #[1, 2, 3, 'Banana', 'Orange', 'Cherry']

list2.append('Mango')
print(list2); #['Banana', 'Orange', 'Cherry', 'Mango']

list2.insert(0, "Apple");
print(list2)#['Apple', 'Banana', 'Orange', 'Cherry', 'Mango']

list2.remove("Mango")
print(list2)# ['Apple', 'Banana', 'Orange', 'Cherry']

print(list2.index("Orange"))#2

print(list2.count("Mango"))#0

list3.sort()
print(list3) #[1, 2, 3, 4, 5, 6, 7, 8, 9]


list2.reverse();
print(list2)#['Cherry', 'Orange', 'Banana', 'Apple']

list3 = list2.copy()
print(list3)#['Cherry', 'Orange', 'Banana', 'Apple']

list2.pop()
print(list2)#['Cherry', 'Orange', 'Banana']

del list2[0]
print(list2) #['Orange', 'Banana']

list2.clear()
print(list2) #[]

del list3
print(list3) #Error => 'list3' is not defined