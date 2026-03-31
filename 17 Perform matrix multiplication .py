import numpy as np # type: ignore

# Input matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Matrix multiplication
result = np.dot(A, B)
# OR you can use: result = A @ B

# Output
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result Matrix:\n", result)