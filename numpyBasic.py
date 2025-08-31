import numpy as np

#1d array
arr_1d=np.array([1,2,3,4,5])


print(arr_1d)



# 2d array
arr_2d=np.array([[1,2],
                 [4,5]])


print(arr_2d)



# multi dimensional array

matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(matrix)

#with defalut value
arr=np.zeros(3)

print(arr)

arr2=np.zeros((2,6))
print(arr2)



#with one value

arr1=np.ones((2,4))

print(arr1)




# full shape

arrfull=np.full((2,4),7)
print(arrfull)

#creating sequence of number in numpy
arrseq=np.arange(1,10,1)
print(arrseq)




# creating identity matrix

arreye=np.eye(4)
print(arreye)