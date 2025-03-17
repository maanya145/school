# Program 2.4
# Given three lists, write a program that adds individual elements of lists 2 and 3 
# to list 1.

list1 = ['a', 'b', 'c']
list2 = ['h', 'i', 't']
list3 = ['0', '1', '2']

print("Originally:")
print("List1 =", list1)
print("List2 =", list2)
print("List3 =", list3)

# Adding elements of list1 at the end of list3
list3.extend(list1)

# Adding elements of list2 at the end of list3
list3.extend(list2)

print("After adding elements of two lists individually, list now is:")
print(list3)
