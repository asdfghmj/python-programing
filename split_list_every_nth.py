def split_list_every_nth(lst, n):
    # Initialize an empty list of lists to hold the result
    result = [[] for _ in range(n)]
    
    # Iterate over the list and distribute elements to the sublists
    for i, element in enumerate(lst):
        result[i % n].append(element)
    
    return result

# Sample list
sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Split every 3rd element
n = 3
# Expected output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
output = split_list_every_nth(sample_list, n)
print(output)
