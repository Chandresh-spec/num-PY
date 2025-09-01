# 👉 Definition:
# NumPy is an open-source Python library that provides support for multi-dimensional arrays (ndarrays), 
# along with a collection of mathematical functions to operate on these arrays efficiently. It allows fast 
# computations on large datasets and is widely used in data science, machine learning, artificial intelligence,
#  statistics, and scientific research.


# difference

# List: Can store different data types in the same list (e.g., int, float, string).
# 
# NumPy Array: Stores only one data type (all elements must be same type → int, float, etc.) for efficiency.





# 2. Performance (Speed & Memory)
# 
# List: Slower, takes more memory (because each element is a Python object).
# 
# NumPy Array: Much faster and memory-efficient (data stored in contiguous blocks like C arrays).



import numpy as np
import time




lst = list(range(1000000))
arr = np.array(lst)

# Multiply each element by 2
start = time.time()
lst = [x*2 for x in lst]
print("List time:", time.time()-start)

start = time.time()
arr = arr * 2
print("Array time:", time.time()-start)


# List time: 0.10057449340820312
# Array time: 0.0019829273223876953

# 4. Functions and Features
# 
# List: Limited built-in functions.
# 
# NumPy Array: Rich functions for math, statistics, linear algebra, random numbers,





# 
# 
# 
# | Feature        | Python List             | NumPy Array                        |
# | -------------- | ----------------------- | ---------------------------------- |
# | Data Type      | Different types allowed | Only one data type                 |
# | Speed & Memory | Slower, more memory     | Faster, less memory                |
# | Operations     | Needs loops             | Vectorized (no loops)              |
# | Functions      | Limited                 | Many (math, stats, linear algebra) |
# | Dimensionality | 1D (nested for higher)  | Supports nD arrays                 |
