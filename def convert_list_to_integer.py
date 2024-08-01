def convert_list_to_integer(lst):
    result = 0
    for num in lst:
        # Determine the number of digits in num
        digits = 1
        temp = num
        while temp >= 10:
            temp //= 10
            digits *= 10
        
        # Shift the current result to the left and add the next number
        result = result * digits * 10 + num
    
    return result

# Sample list
sample_list = [11, 33, 50]
# Expected output: 113350
output = convert_list_to_integer(sample_list)
print(output)
