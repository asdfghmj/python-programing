def insert_string_at_beginning(lst, string):
    # Use a list comprehension to add the string to each element in the list
    result = [string + str(item) for item in lst]
    return result

# Sample list
sample_list = [1, 2, 3, 4]
# String to be inserted
string = 'emp'
# Expected output: ['emp1', 'emp2', 'emp3', 'emp4']
output = insert_string_at_beginning(sample_list, string)
print(output)
