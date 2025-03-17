# Program 2.3
# Given three lists, write a program that adds lists 2 and 3 to list 1 
# as single elements each.

list1 = ['a', 'b', 'c']
list2 = ['h', 'i', 't']
list3 = ['0', '1', '2']

print("Originally:")
print("List1 =", list1)
print("List2 =", list2)
print("List3 =", list3)

# Adding list2 as a single element at the end of list1
list1.append(list2)

# Adding list3 as a single element at the start of list1
list1.insert(0, list3)

print("After adding two lists as individual elements, list now is:")
print(list1)
