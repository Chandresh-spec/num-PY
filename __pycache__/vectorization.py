# # Vectorization means applying operations directly on entire arrays (vectors, matrices, tensors) without using Python for loops.


# NumPy uses optimized C code under the hood, so vectorized operations are much faster than looping in pure Python.

# 👉 In short: one line of NumPy code = hundreds of loop iterations in Python.




import numpy as np

a = [1, 2, 3, 4, 5]
b = []

for x in a:
    b.append(x**2)

# print(b)  # [1, 4, 9, 16, 25]


a=np.array([1,2,3,4,5,6])
b=a**2

print(b)