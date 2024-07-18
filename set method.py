# create a set
my_set = {1, 2, 3}

# add an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# clear the set
my_set.clear()
print(my_set)  # Output: set()

# create a new set
my_set = {1, 2, 3}

# create a copy of the set
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

# Demonstrating difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)  # Output: {1, 2}

# Demonstrating difference_update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print("Set1 after difference_update:", set1)  # Output: {1, 2}

# Demonstrating discard()
set1 = {1, 2, 3}
set1.discard(2)
print("Set1 after discarding 2:", set1)  # Output: {1, 3}

# Demonstrating intersection()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)  # Output: {3}

# Demonstrating intersection_update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print("Set1 after intersection_update:", set1)  # Output: {3}

# Demonstrating isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
are_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", are_disjoint)  # Output: True

#issubset()
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"mango", "orange", "apple", "banana", "cherry"}
print(fruits1.issubset(fruits2)) # True

# <=
print(fruits1 <= fruits2) # True

# <
fruits3 = {"apple", "banana"}
print(fruits3 < fruits1) # True

# issuperset()
print(fruits2.issuperset(fruits1)) # True

# >=
print(fruits2 >= fruits1) # True

# >
print(fruits1 > fruits3) # True

# pop()
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x) # Removes a random element
print(fruits) # The set with the removed element
# remove()
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # Output: {'apple', 'cherry'}

# symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # Output: {'banana', 'cherry', 'microsoft', 'google'}

# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
print(x) # Output: {'cherry', 'banana', 'microsoft', 'google'}

# union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) # Output: {'cherry', 'banana', 'google', 'microsoft', 'apple'}

# update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x) # Output: {'cherry', 'banana', 'google', 'microsoft', 'apple'}
