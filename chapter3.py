# Fnacy indexing
import numpy as np
 

a=np.array([1,2,3,4,5,6])

print(a[[1,2,3,4]])



# boolena masking
num=a[a>4]
print(num)







# reshaping and manipulating array



# arr=np.array([[1,2,3,4,5,6],
            #   [4,5,6,4,9,3]])
# 
# num=arr.reshape((3,3))
# print(num)




#flattering array

arr=np.array([[1,2,3,4,5,6]])

arr.ravel()
print(arr)