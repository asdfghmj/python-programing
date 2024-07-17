# identify if matrix is symmetry take input from user for size mxn of matrix and also matrix values and also check if no column is equal to number of row (write the code in minium lines)

def is_symmetric(matrix):
  return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(i + 1, len(matrix[0])))

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
if rows != cols:
  print("Matrix is not square, cannot be symmetric.")
else:
  matrix = [[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]
  print("The matrix is symmetric." if is_symmetric(matrix) else "The matrix is not symmetric.")
