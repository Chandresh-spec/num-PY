import numpy as np


arr = np.array([[1, 2, 3],
                [4, 5, 6]])


print(arr.reshape(-1))




arr = np.array([[1, 2], [3, 4]])


flat=arr.flatten()

print(flat)

print(arr)




arr = np.array([[1, 2, 3],
                [4, 5, 6]])


print(arr.reshape(-1))




arr = np.array([[1, 2], [3, 4]])


flat=arr.ravel()

print(flat)

print(arr)