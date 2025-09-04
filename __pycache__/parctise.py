import numpy as np

arr=np.array([1,2,3,4])



print(arr)



arr2d=np.array([[1,2,3],
                [2,4,6]])


print(arr2d)


matrix=np.array([[[1,2,3],
         [4,4,6]],
        [ [4,8,9],
         [8,9,3]]])


print(matrix)



default0=np.zeros((2,6))

print(default0)



default1=np.ones((3,3))
print(default1)



defall=np.full((2,3),10)

print(defall)



#creating sequence of number in numpy


seq=np.arange(2,10)

print(seq)


iden=np.identity(5)

print(iden)

matrix=np.array([[[1,2,3],
         [4,4,6]],
        [ [4,8,9],
         [8,9,3]]])

print(matrix.shape)



sizele=np.array([[1,2,3,45],
                 [4,5,6,55]])


print(sizele.size)