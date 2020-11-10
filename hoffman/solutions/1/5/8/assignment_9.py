import numpy as np 
A = np.array([[1,2],[3,4]])
det  = np.linalg.det(A)
if(det == 0):
    print("Inverse doesn't exist as determinant is zero\n")
else:
    print("Determinant of given matrix is not zero, So, The inverse is : \n", np.linalg.inv(A)) 