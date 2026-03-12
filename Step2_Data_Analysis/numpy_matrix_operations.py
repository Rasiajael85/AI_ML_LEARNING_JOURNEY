import numpy as np

# create two matrices
A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[7,8,9],
              [1,2,3]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# addition
print("Matrix Addition:\n", A + B)

# subtraction
print("Matrix Subtraction:\n", A - B)

# multiplication
print("Matrix Multiplication:\n", A * B)

# transpose
print("Transpose of A:\n", A.T)