def is_palindrome(number):
  number_str = str(number)
  reversed_str = number_str[::-1]
  return number_str == reversed_str
number = 12321
if is_palindrome(number):
  print("The number", number, "is a palindrome.")
else:
  print("The number", number, "is not a palindrome.")

number = 12
if is_palindrome(number):
  print("The number", number, "is a palindrome.")
else:
  print("The number", number, "is not a palindrome.")
