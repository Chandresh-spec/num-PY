# In NumPy, arrays are fixed-size once created (unlike Python lists). That means you can’t directly “remove” an element in place.
# Instead, NumPy creates a new array without that element using functions like np.delete().

# numpy.delete(arr, obj, axis=None)
# 
# arr → input array
# 
# obj → index (or list of indices) of elements to remove
# 
# axis → if None, array is flattened first
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])

a=np.delete(arr,1,axis=0)




print(a)