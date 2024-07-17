#  if it symetric matrix or not

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

# Example usage
matrix1 = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]
matrix3=[[4 , 5 , 4 , 8 ],
          [5 , 5 , 3 , 7  ],
          [4 , 3 , 4 , 9 ],
          [ 8 , 7 , 9 ,11]]

if is_symmetric(matrix1):
  print("Matrix 1 is symmetric.")
else:
  print("Matrix 1 is not symmetric.")


if is_symmetric(matrix3):
  print("Matrix 3 is symmetric.")
else:
  print("Matrix 3 is not symmetric.")
