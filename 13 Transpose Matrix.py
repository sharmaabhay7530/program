try:
    import numpy as np
except ImportError:
    np = None

if np is not None:
    print("Transpose (numpy):\n", np.array([[1, 2], [3, 4]]).T)
else:
    matrix = [[1, 2], [3, 4]]
    transpose = [list(row) for row in zip(*matrix)]
    print("Transpose (pure Python):\n", transpose)

# input: np.array([[1, 2], [3, 4]]) (if numpy available)
# output: [[1, 3], [2, 4]]
