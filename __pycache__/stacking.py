# In NumPy, stacking means joining arrays along a new axis.
# It is similar to concatenation, but concatenation joins along existing axes, while stacking adds a new axis.


# Main stacking functions in NumPy

# np.stack() → Join along a new axis you specify.

# np.hstack() → Stack arrays horizontally (along columns).

# np.vstack() → Stack arrays vertically (along rows).

# np.dstack() → Stack arrays along depth (3rd axis).




import numpy as np
# 
# ✅ 1. np.stack()
a=np.array([1,2,3,4,5])
b=np.array([4,5,6,1,4])

res=np.stack((a,b),axis=1)
print(res)





# ✅ 2. Horizontal stacking → np.hstack()

c=np.array([4,5,6,1])
d=np.array([9,6,3,2])

e=np.hstack((c,d))


print(e)


# ✅ 3. Vertical stacking → np.vstack()


c=np.array([4,5,6,1])
d=np.array([9,6,3,2])

e=np.vstack((c,d))


print(e)

# 
# ✅ 4. Depth stacking → np.dstack()



c=np.array([4,5,6,1])
d=np.array([9,6,3,2])

e=np.dstack((c,d))


print(e)
