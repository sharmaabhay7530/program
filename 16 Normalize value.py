import numpy as np # type: ignore

# Input array
arr = np.array([10, 20, 30, 40, 50])

# Normalization
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

# Output
print("Original Array:", arr)
print("Normalized Array:", normalized_arr)