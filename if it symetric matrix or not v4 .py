# if it symetric matrix or not .user input the size and mat

def is_symmetric(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  if rows != cols:
    return False
  for i in range(rows):
    for j in range(i + 1, cols):
      if matrix[i][j] != matrix[j][i]:
        return False

  return True

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the matrix elements:")
for i in range(rows):
  row = []
  for j in range(cols):1
    element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
    row.append(element)
  matrix.append(row)

if is_symmetric(matrix):
  print("The matrix is symmetric.")
else:
  print("The matrix is not symmetric.")

