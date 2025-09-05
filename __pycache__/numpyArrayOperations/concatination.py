# ChatGPT said:

# In NumPy, concatenation means joining two or more arrays into one.
 # For this, NumPy provides the function:


# syntax
# np.concatenate(arr1,arr2,....,axis=0,out=None)


# Parameters:
# 
# (a1, a2, …) → Sequence of arrays you want to join.
# 
# axis → The axis along which to join. Default is 0.
# 
# out → Optional output array.

import numpy as np

n1=np.array([[1,2,5],[2,4,5]])

n2=np.array([[7],[5]])

res=np.concatenate((n1,n2),axis=1)

print(res)
