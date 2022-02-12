import numpy as n

zeroDim = 69
oneDim = [5,1,7,9,3]
twoDim = [[5,1,7,9,3],[2,4,6,8,10]]
threeDim = [[[5,1,7,9,3],[2,4,6,8,10]],[[111,222,333,444],[11,22,33,44]]]

dim1 = n.array(oneDim)
print(dim1.ndim,dim1)

dim2 = n.array(twoDim)
print(dim2.ndim,dim2)

dim3 = n.array(threeDim)
print(dim3.ndim,dim3)

