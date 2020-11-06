import numpy as np

A=np.array([[2,0,1j],[1,-3,-1j],[1j,1,1]])
Ainv=np.linalg.inv(A)
I=A@Ainv
print(Ainv)

