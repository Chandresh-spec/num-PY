import numpy as np
# 
# 
# arr=np.full((3,3),7)

# arr=np.arange(1,9,3)
# 
# print(arr)
# 
# 
# 
# 
# identity matrixs
# 
# identity_mat=np.eye(4,dtype=float)
# 
# print(identity_mat)
# 
# 
# 
# 
# array checking
# 
# arrshape=np.array([[1,2,3,1],[7,8,9,6]])
# 
# print(arrshape.shape)
# 
# 
# 
# 
# 
# size

# it return the total number of element in the array
# 
# arrsize=np.array([[1,2,3],[8,9,6]])
# 
# print(arrsize.size)
# 
# 
# dtype()
# it return the type of array
# 
# n=np.array([1.2,5.3,1.8])
# 
# print(n.dtype)
# 
# 
# 
# 
# 
# ndim it return the number of dimesion in the array
# it return 1d array 2d array and multi dimensional array
# 
# 
# dimarr=np.array([[[1,2,3],[4,7,9]],[
                #  [7,8,9],[5,6,3]]])
# 
# 
# print(dimarr.ndim)
# 
# changing type conversion
# 
# arr=np.array([1,2,3,4,5,6])
# 
# newarr=arr.astype(str)
# 
# 
# print(newarr)
# 
# 
# 
# 
# matmatics
# a=np.array([10,20,30])
# b=np.array([2,5,3])
# 
# c=a**b
# print(c)
# 
# 
# fancy=np.array([[1,2,5,8,9,3],[5,8,9,5,6,8]])
# print(fancy)
# res=fancy[[0,0,1],[2,4,2]]
# print(res)
# 
# it return the copy not view
# 
# 
# 
# 
# boolean masking
# 
# 
# 
# lst=np.array([1,5,8,9,6,3,2,14])
# 
# mask=(lst>4) & (lst<10)
# 
# print(lst[mask])


arr2=np.array([[1,2,5,8,9,3],[5,8,9,5,6,8]])


mask=(arr2>4) & (arr2<9)

print(arr2[mask])
# where  return the index


store=np.where(arr2>7)


print(store)


print(arr2[store])


# 
# replace the value with mask




arr3=np.array([[1,2,5,8,9,3],[5,8,9,5,6,8]])


mask=(arr3>4)

arr3[mask]=0
print(arr3)

