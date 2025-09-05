import numpy as np


# arr=np.array([1,2,4,5,6])
# 
# newarr=np.append(arr,[4,5,6,3,1,2])
# 
# print(newarr)
# 


#2d matrixs append


a=np.array([[1,2,3,4,5],
            [8,9,6,3,6]])

b=np.append(a,[[7,3,4,8,9],[2,5,8,9,6]],axis=1)


print(b)




# Key Points:
# 
# append() always adds at the end.
# 
# insert() lets you add values anywhere.
# 
# Both return a new array, they don’t modify the original one.
# 
# If axis=None, both arr and values are flattened before appending.