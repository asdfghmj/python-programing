def is_symmetric(matrix):
    n = len(matrix)
    return all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(i + 1, n))

n = int(input("Enter the size of the matrix: "))

matrix = [[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
