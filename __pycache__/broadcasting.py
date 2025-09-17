# 🔹 What is Broadcasting?

# Broadcasting is the automatic expansion of smaller arrays so they can match the shape of larger arrays during arithmetic operations.
# # 👉 It saves you from writing loops and allows vectorized operations.


import numpy as np

a = np.array([1, 2, 3])
b = 2 



# 🔹 Rule of Broadcasting
# 
# When operating on two arrays:
# 
# Compare shapes element-wise from the end.
# 
# They are compatible if:
# 
# They are equal, OR
# 
# One of them is 1.
# 
# If compatible, NumPy stretches the smaller shape.


a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2,3)

b = np.array([10, 20, 30])



print(a + b)