# Check if a number is Palindrome floor division

def is_palindrome_floor_division(number):
  reversed_number = 0
  original_number = number
  while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number //= 10
  return original_number == reversed_number

number = 12321

if is_palindrome_floor_division(number):
  print("The number", number, "is a palindrome.")
else:
  print("The number", number, "is not a palindrome.")

number = 12
if is_palindrome_floor_division(number):
  print("The number", number, "is a palindrome.")
else:
  print("The number", number, "is not a palindrome.")
