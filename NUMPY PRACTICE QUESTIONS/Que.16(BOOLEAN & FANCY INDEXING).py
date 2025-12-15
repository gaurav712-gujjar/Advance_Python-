import numpy as np

#1. Select all elements greater than 25 from a NumPy array.

arr = np.random.randint(1, 100, 50)
print(arr[arr>25])
