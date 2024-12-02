# new-folder
day1 python 
# day 1 i have learn in python what is variable
# strings, lists[],sets{},dictionarys{},tuples()
# variables
# variable is a container that holds a value
# variable is a name given to a value
# a = 5
# print(type(a), "a value is :" ,a)
# strings :
# strings are sequence of characters
# strings are enclosed in single quotes or double quotes
# strings are immutable
# str = ["vishnu","vardhan"]
# print(len(str)) 
# #output is 2
# str1='hello'
# print(str1[:-1])
# strings methods are :
# 1. capitalize():Converts the first character to uppercase.
# text = "hello , World"
# print(text.upper())
# lower:
# print(text.lower())
# 2. find():Returns the lowest index of the substring if found, otherwise -1.
# print(text.find("World"))
# 3. isalnum():Returns True if all characters in the string are alphanumeric, meaning alphabet
# letter (a-z) and numerals (0-9). Returns False otherwise.:
# print(text.isalnum())
# 4. isalpha():Returns True if all characters in the string are alphabets,
# meaning a-z or A-Z. Returns False otherwise
# print(text.isalpha())
#  replace():Replaces all occurrences of a substring with another substring.
# print(text.replace("o","j"))
# 4. split():Splits the string at the specified separator and returns a list.
# LISTS: Lists are used to store multiple items are one of 4 built  in data types in python.Used to store collections of data the other 3 are Tuple,Sets and Dicionary all with the different and usage
Lists= [22,23,5,8,11,99]
# Lists.sort()
# print(Lists)
# Append: Adds an element to the end of the list.
# Lists.append(0)
# print(Lists) #[22, 23, 5, 8, 11, 99, 0]
# Insert: Inserts an element at a specified position.
# Lists.insert(1,"z")
# print(Lists) #[22, 'z', 23, 5, 8, 11, 99, 0]
# Remove: Removes the first occurrence of a value
# Lists.remove(99)
# Clear: Removes all elements from the list.
# print(Lists) #[22, 23, 5, 8, 11]
# Lists.clear()
# print(Lists) #[ ]
#index:  ReturLists.index(2)
# print(Lists.index(22)) #0
# Pop: Removes and returns the element at the specified position. If no index is specified, it removes and returns the last item.
# Lists.pop()
# print(Lists) #[22, 23, 5, 8, 11]
# Count: Returns the number of occurrences of a specified value.
# print(Lists.count(23)) #1
# Reverse: Reverses the order of elements in the list.
# Lists.reverse()
# print(Lists) #[11, 8, 5, 23, 22]
# extend: is used to add multiple values into a tuple
# Lists.extend([25,2024])
# print(Lists)
# Sets:The set data type is a collection that is unordered, mutable, and contains unique elements. Sets are highly useful for operations like membership testing, deduplication, and mathematical set operations such as union, intersection, and difference.
sets = {1 , 2, 4}
# print(sets)
# => add(element): Adds a single element to the set.
# sets.add(50)
# print(sets) #{1, 2, 4, 50}
# update(iterable): Adds multiple elements from an iterable to the set
# sets.update([5,80])
# print(sets) #{1, 2, 4, 50, 5,80}
# remove(element): Removes a specified element. Raises KeyError if the element is not present.
# sets.remove(1)
# print(sets) #{2, 4}
# discard(element): Removes a specified element but doesn't raise an error if the element is not present.
# sets.discard(1)
# print(sets)
# pop(): Removes and returns an arbitrary element. Raises KeyError if the set is empty
# sets.pop()
# print(sets) 
# clear(): Removes all elements from the set
# sets.clear()
# print(sets) #{ }
# Set Operations
# union(*others): Returns a new set that is the union of the sets.
lets check on chatgpt
TUPLES
> TUPLES are immutable , we can't change the value  .
 >Tuples are ordered, immutable, and contain unique elements. They are defined by enclosing elements in
 parentheses, and they are used to store a collection of elements that should not be changed after creation.
 >it does not support to insert number.
 >we can't change of it.
 # Creating a tuple
t = (1, 2, 3, 4, 2)

# Using methods
print(t.count(2))        # Output: 2
print(t.index(3))        # Output: 2

# Slicing
print(t[1:3])            # Output: (2, 3)

# Concatenation
t2 = (5, 6)
print(t + t2)            # Output: (1, 2, 3, 4, 2, 5, 6)

# Tuple unpacking
a, b, c, d, e = t
print(a, b, c, d, e)     # Output: 1 2 3 4 2
# dictionary:
In Python, a dictionary is an unordered, mutable collection used to store data in key-value pairs. Each key in a dictionary is unique, and it is associated with a specific value. Dictionaries are denoted using curly braces {}.

Key Features of Dictionaries
Unordered: The items are stored without a specific order (until Python 3.7, where insertion order is maintained).
Keys must be immutable: Keys can be strings, numbers, or tuples (if the tuple contains only immutable elements).
Values can be any type: Values can be any data type, including other dictionaries or lists.
Creating a Dictionary
Using curly braces:
python
Copy code
d = {"name": "Vishnu", "age": 25}
Using the dict() constructor:
python
Copy code
d = dict(name="Vishnu", age=25)
Empty dictionary:
python
Copy code
d = {}
Accessing and Modifying Data
Access a value using a key:

python
Copy code
d = {"name": "Vishnu", "age": 25}
print(d["name"])  # Output: Vishnu
If the key does not exist, it raises a KeyError.
Using get() to access a value:

python
Copy code
print(d.get("name"))  # Output: Vishnu
print(d.get("gender", "Not specified"))  # Output: Not specified
Add or update a key-value pair:

python
Copy code
d["gender"] = "Male"  # Add
d["age"] = 26         # Update
print(d)  # {"name": "Vishnu", "age": 26, "gender": "Male"}
Remove a key-value pair:

pop(key): Removes the specified key and returns its value.
python
Copy code
age = d.pop("age")
print(age)  # Output: 26
print(d)  # {"name": "Vishnu", "gender": "Male"}
popitem(): Removes and returns the last inserted key-value pair (Python 3.7+).
python
Copy code
key_value = d.popitem()
print(key_value)  # Output: ("gender", "Male")
Delete a key or clear the dictionary:

python
Copy code
del d["name"]  # Deletes a specific key
d.clear()      # Clears all key-value pairs
print(d)       # Output: {}
Dictionary Methods
Keys, Values, and Items

keys(): Returns a view object of all keys.
python
Copy code
d = {"name": "Vishnu", "age": 25}
print(d.keys())  # Output: dict_keys(['name', 'age'])
values(): Returns a view object of all values.
python
Copy code
print(d.values())  # Output: dict_values(['Vishnu', 25])
items(): Returns a view object of all key-value pairs as tuples.
python
Copy code
print(d.items())  # Output: dict_items([('name', 'Vishnu'), ('age', 25)])
Check if a key exists:

Use the in operator to check for a key.
python
Copy code
print("name" in d)  # Output: True
print("gender" not in d)  # Output: True
Update a dictionary:

Use update() to merge another dictionary or key-value pairs.
python
Copy code
d.update({"gender": "Male", "age": 26})
print(d)  # Output: {'name': 'Vishnu', 'age': 26, 'gender': 'Male'}
Copy a dictionary:

copy() creates a shallow copy of the dictionary.
python
Copy code
d_copy = d.copy()
print(d_copy)  # Output: {'name': 'Vishnu', 'age': 26, 'gender': 'Male'}
Dictionary Operations
Iterate through a dictionary:

Iterate over keys:
python
Copy code
for key in d:
    print(key)
Iterate over values:
python
Copy code
for value in d.values():
    print(value)
Iterate over key-value pairs:
python
Copy code
for key, value in d.items():
    print(f"{key}: {value}")
Length of a dictionary:

python
Copy code
print(len(d))  # Output: 3
Example Usage
python
Copy code
# Create a dictionary
student = {"name": "Vishnu", "age": 25, "grade": "A"}

# Access and modify
print(student["name"])  # Vishnu
student["age"] = 26
student["gender"] = "Male"

# Add or remove
student.pop("grade")

# Iterate
for key, value in student.items():
    print(f"{key}: {value}")

# Output
# name: Vishnu
# age: 26
# gender: Male
Dictionaries are extremely versatile and are commonly used for structured data, configurations, and mapping relationships.










