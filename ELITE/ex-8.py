#LISTS

# 1.creating lists
empty_list=[]
numbers =[1,2,4,5]#mutable--we can change
fruits=["apple","banana","cherry"]
mixed_list=[1,"hello",3.14,True]
# 2.acessing elements
fruits=["apple","banana","cherry"]
print(fruits[0])#output : "apple"
# 3.slicing lists
numbers =[1,2,3,4,5]
print(numbers[1:4])#output:[2,3,4]
# 4.modifying elements
fruits=["apple","banana","cherry"]
fruits[0]="orange"
print(fruits)#output :["orange","banana","cherry"]
# 5.list concatenation
list1 =[1,2,3]
list2 =[4,5,6]
combined_list=list1+list2
print(combined_list)#output :[1,2,3,4,5,6]

# Define two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Append an element to list1
list1.append(6)
print("List1 after appending:", list1)

# Insert an element into list2
list2.insert(2, 10)
print("List2 after inserting:", list2)

# Remove an element from list1
list1.remove(3)
print("List1 after removing:", list1)

# Pop an element from list2
popped_element = list2.pop()
print("Popped element from List2:", popped_element)
print("List2 after popping:", list2)

# Find the index of an element in list1
index = list1.index(4)
print("Index of 4 in List1:", index)

# Count occurrences of an element in list2
count = list2.count(5)
print("Count of 5 in List2:", count)

# Sorting list1
list1.sort()
print("Sorted List1:", list1)

# Reversing list2
list2.reverse()
print("Reversed List2:", list2)

#length
length = len(list1)   # Returns the length of the list

#clearing
#length = len(my_list)   # Returns the length of the list
