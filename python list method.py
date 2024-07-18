fruits = ['apple', 'banana', 'cherry']

# append()
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

# clear()
fruits.clear()
print(fruits) # Output: []

# copy()
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy) # Output: ['apple', 'banana', 'cherry']

# count()
print(fruits.count("cherry")) # Output: 1

# extend()
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits) # Output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# index()
print(fruits.index("cherry")) # Output: 2

# insert()
fruits.insert(1, "orange")
print(fruits) # Output: ['apple', 'orange', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo'] 

# List of integers
numbers = [1, 2, 3, 4, 5]

# pop() - Removes and returns the element at the specified position
removed_element = numbers.pop(2)  # Removes the element at index 2 (value 3)
print("Removed element:", removed_element)
print("List after pop():", numbers)  # Output: [1, 2, 4, 5]

# remove() - Removes the first occurrence of the specified value
numbers.remove(4)  # Removes the value 4
print("List after remove():", numbers)  # Output: [1, 2, 5]

# reverse() - Reverses the order of the list
numbers.reverse()
print("List after reverse():", numbers)  # Output: [5, 2, 1]

# sort() - Sorts the list in ascending order
numbers.sort()
print("List after sort():", numbers)  # Output: [1, 2, 5]
