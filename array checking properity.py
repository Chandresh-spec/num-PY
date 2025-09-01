#shape
# return the number of rows and colum in integeer, basically it return how many rows and colum exist in the array
import numpy as  np
# one dimension
arrshape=np.array([1,2,3,5,4,7])
print(arrshape.shape)


# two dimension

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(arr.shape)

#multi dimensions 

arr=np.array([[[1,2,7,8],
              [8,8,9,5]],
              [[4,5,6,4],
              [8,9,6,1]]])

print(arr.shape)








#size 
# basically it return the total number of element in the array
# one dimension
arrsize=np.array([1,2,3,5,4,7])
print(arrsize.size)





# two dimension

arrs=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(arrs.size)



#multi dimensions 

arr3=np.array([[[1,2,7,8],
              [8,8,9,5]],
              [[4,5,6,4],
              [8,9,6,1]]])

print(arr3.size)



#dtype   
# it return type of array ..example int str float like


n=np.array(["1",'5'])
print(n.dtype)





# ndim 

# it return the number of dimension in the array
# it return 1d array 2d array 3d array
arrd=np.array([1,2,3,5,4])


print(arrd.ndim)






