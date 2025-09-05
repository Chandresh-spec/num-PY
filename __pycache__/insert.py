import numpy as np


arr=np.array([1,2,3,4])

newarr=np.insert(arr,1,100,axis=None)
print(newarr)

arr2=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])


new2darr=np.insert(arr2,2,[6,3,9],axis=1)


print(new2darr)



a=np.array([1,2,3,4,5])

b=np.insert(a,(2,4),(100,200))

print(b)



arr=np.array([[1,2,4,5,6],
              [4,8,9,6,4]])


d=np.insert(arr,3,[7,8,9,6,8],axis=0)
print(d)