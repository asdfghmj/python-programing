# Accessing elements
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(my_dict["brand"])  # Output: Ford
print(my_dict.get("model"))  # Output: Mustang (using get() method)

# Changing elements
my_dict["year"] = 2020
print(my_dict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Adding elements
my_dict["color"] = "red"
print(my_dict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}

# Removing elements
del my_dict["model"]
print(my_dict)  # Output: {'brand': 'Ford', 'year': 2020, 'color': 'red'}
popped_item = my_dict.pop("year")
print(popped_item)  # Output: 2020
print(my_dict)  # Output: {'brand': 'Ford', 'color': 'red'}
my_dict.popitem()  # Removes the last inserted item
print(my_dict)  # Output: {'brand': 'Ford'}

# Looping through a dictionary
for key in my_dict:
  print(key)  # Prints keys: brand

for value in my_dict.values():
  print(value)  # Prints values: Ford

for key, value in my_dict.items():
  print(key, value)  # Prints key-value pairs: brand Ford

# Copying a dictionary
new_dict = my_dict.copy()
print(new_dict)  # Output: {'brand': 'Ford'}

# Nested dictionaries
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(my_family["child2"]["name"])  # Output: Tobias

# Dictionary methods
my_dict.clear()  # Clears the dictionary
print(my_dict)  # Output: {}

keys = ('key1', 'key2', 'key3')
values = 0
new_dict = dict.fromkeys(keys, values)
print(new_dict)  # Output: {'key1': 0, 'key2': 0, 'key3': 0}

print(my_family.get("child1"))  # Output: {'name': 'Emil', 'year': 2004}
print(my_family.items())  # Output: dict_items([('child1', {'name': 'Emil', 'year': 2004}), ...])
print(my_family.keys())  # Output: dict_keys(['child1', 'child2', 'child3'])

my_family.pop("child3")  # Removes 'child3' and its value
print(my_family)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}}

item = my_family.popitem()  # Removes and returns the last inserted item
print(item)  # Output: ('child2', {'name': 'Tobias', 'year': 2007})

my_family.setdefault("child4", "New child")  # Inserts 'child4' if it doesn't exist
print(my_family)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child4': 'New child'}

my_family.update({"child5": {"name": "Alice", "year": 2015}})  # Updates or adds items
print(my_family)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child4': 'New child', 'child5': {'name': 'Alice', 'year': 2015}}

print(my_family.values())  # Output: dict_values([{'name': 'Emil', 'year': 2004}, 'New child', {'name': 'Alice', 'year': 2015}])
