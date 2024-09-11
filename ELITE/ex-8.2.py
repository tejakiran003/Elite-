#DICTIONARIES

# 1.creating Dictionaries:
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_dict1 = { 'name': 'Harry', 'age': '11','house': 'Gryffindor'}
print(my_dict)
print(my_dict1)
# 2.Acessing Values
print(my_dict["key1"])   # Accessing the value associated with "key1"
name_value = my_dict1['name']
age_value = my_dict1['age']
house_value = my_dict1['house']
# 3.Adding values
my_dict["new_key"] = "new_value"   # Adding a new key-value pair
my_dict1['gender'] = 'Male'
# 4.Modifying values
my_dict["key1"] = "modified_value"   # Modifying the value associated with "key1"
my_dict1['age']= 12

#OPERATIONS

# Define two dictionaries
dict1 = {"name": "Alice", "age": 30, "city": "New York"}
dict2 = {"name": "Bob", "age": 25, "city": "Los Angeles", "country": "USA"}

# Accessing Elements
print("Name of dict1:", dict1["name"])
print("Age of dict2:", dict2["age"])

# Adding or Modifying Elements
dict1["gender"] = "Female"  # Adding a new key-value pair to dict1
dict2["age"] = 26  # Modifying the value associated with the "age" key in dict2
print("dict1 after adding/modifying:", dict1)
print("dict2 after adding/modifying:", dict2)

# Removing Elements
del dict1["city"]  # Deleting the "city" key from dict1
print("dict1 after deleting:", dict1)

# Checking if a Key Exists
if "country" in dict2:
    print("Country key exists in dict2")

# Dictionary Methods
print("Keys of dict1:", dict1.keys())
print("Values of dict2:", dict2.values())
print("Items of dict1:", dict1.items())

# Length of a Dictionary
print("Length of dict2:", len(dict2))

# Clearing a Dictionary
dict2.clear()
print("dict2 after clearing:", dict2)

#LOOPING
for key in my_dict:
    print(key)
#loop through values
for value in my_dict.values():
    print(value)
#loop through key_value pairs
for key,value in my_dict.items():
    print(key,value)
    
#COMPREHENSIONS
squares_dict ={x:x**2 for x in range(1,6)}
print(squares_dict)