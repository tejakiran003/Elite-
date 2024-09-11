
#SETS - USING {} or ()

# 1.creating an empty set 
empty_set =set()
# 2.creating a set with elements
fruits ={'apple','banana','cherry'}
# 3.creating a set from a list
numbers = set([1,2,3,4,5])
# 4.adding elements
my_set={1,2}
my_set.add(3)
print(my_set) #output :{1,2,3}
# 5.removing elements
my_set={1,2,3}
my_set.remove(2)
print(my_set) #output :{1,3}

# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference (set1 - set2)
difference_set1 = set1 - set2
print("Difference (set1 - set2):", difference_set1)

# Difference (set2 - set1)
difference_set2 = set2 - set1
print("Difference (set2 - set1):", difference_set2)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)

# Subset
is_subset = set1 <= set2
print("Is set1 a subset of set2?", is_subset)

# Superset
is_superset = set1 >= set2
print("Is set1 a superset of set2?", is_superset)

'''
SET METHODS
pop(),clear(),copy(),update(),etc.
'''
