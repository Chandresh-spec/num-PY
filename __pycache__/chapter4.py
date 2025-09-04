#Fancy indexing
import numpy as np

arr=np.array([1,2,3,4,5])

print(arr[[2,0,4]])


#2d array

arr2=np.array([[1,2,3,4],
              [5,6,1,8],
              [8,6,9,5]])


print(arr2[[1,1,0],[2,0,3]])