def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
