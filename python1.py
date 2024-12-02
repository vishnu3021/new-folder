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
# Tuples:
# t=(1,23,50,8,90,36,55)
# print(t)
# print(t[1])
# print(t[:-1])
# print(t*60)
# DIctionary:
d={"name":"John","age":30,"city":"New York"}
print(d["name"])
print(d.get("gender","male"))
print(d.pop("city"))
print(d.items())
print(d.keys())
print(d.values())
print(d.update({"age":40,"city":"Los Angeles"}))
print(d)
del d["city"]
print(d)
print('name' in d)
print('name' not in d)
dd = d
print(dd)
for key in d:
    print(key,d[key])
    print(key)

for value in d.values():
    print(value)
    print("values are :")
for key,value in d.items():
    print(key,value)
    print(f'{key}:{value}')
    