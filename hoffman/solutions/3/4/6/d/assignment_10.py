# Let T be the linear operator on R^2 defined by T(x1,x2)=(−x2,x1). 
# Prove that if β is any ordered basis for R^2 and [T]β =A then A12*A21 is not 0.
import numpy as np

arr = np.array([[4,6,-2,-8],[2,8,4,6]], dtype = float)
arr[0] = arr[0]/4
arr[1] = arr[1] - arr[0]*2
arr[1] = arr[1]*4/20
arr[0] = arr[0] - arr[1]*6/4
print("A12*A21 = ", arr[0,3]*arr[1,2])
print("We can see that it is not zero.")