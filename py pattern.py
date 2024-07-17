# Square Pattern
n = 5
for i in range(n):
  for j in range(n):
    print("*", end=" ")
  print()

# Right Triangle Pattern
n = 5
for i in range(n):
  for j in range(i + 1):
    print("*", end=" ")
  print()

# Inverted Right Triangle Pattern
n = 5
for i in range(n):
  for j in range(n - i):
    print("*", end=" ")
  print()

# Pyramid Pattern
n = 5
for i in range(n):
  for j in range(n - i - 1):
    print(" ", end=" ")
  for j in range(2 * i + 1):
    print("*", end=" ")
  print()

# Diamond Pattern
n = 5
for i in range(n):
  for j in range(n - i - 1):
    print(" ", end=" ")
  for j in range(2 * i + 1):
    print("*", end=" ")
  print()

for i in range(n - 1):
  for j in range(i + 1):
    print(" ", end=" ")
  for j in range(2 * (n - i - 1) - 1):
    print("*", end=" ")
  print()

# Number Pattern 1
n = 5
num = 1
for i in range(n):
  for j in range(i + 1):
    print(num, end=" ")
    num += 1
  print()

# Number Pattern 2
n = 5
for i in range(n):
  num = 1
  for j in range(i + 1):
    print(num, end=" ")
    num += 1
  print()

# Character Pattern
n = 5
ch = 'A'
for i in range(n):
  for j in range(i + 1):
    print(ch, end=" ")
  ch = chr(ord(ch) + 1)
  print()
