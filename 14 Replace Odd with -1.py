import numpy as np # type: ignore

arr = np.array([1, 2, 3, 4, 5])
arr[arr % 2 != 0] = -1

print(arr)





