import numpy as np

arr=np.array([1,2,5,4,8,6,3])

mask=arr<4

print(mask)

print(arr[mask])


#multiple condition 



mask =(arr>4 ) |  (arr < 8)

print(mask)



# 2 day array filtering
arr2=np.array([[1,2,3,4],
               [7,8,9,6],
               [6,3,5,4]])

mask=(arr2>1) & (arr2<5)

print(arr2[mask])
print(arr2)





# using where 



arr2=np.array([1,5,8,9,6,3,2,4])

ind=np.where(arr2<5)
print(arr2[ind])

print(ind)





# Replace values with mask


arr3=np.array([1,2,5,4,6,84,2,0])


arr3[arr3>5]=0
print(arr3)