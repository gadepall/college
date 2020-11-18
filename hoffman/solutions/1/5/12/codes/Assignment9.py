from scipy.linalg import hilbert
import numpy as np
from fractions import Fraction 

#form a 3x3 Hilbert matrix
Ainv=1
for k in range(1,5):
    A=hilbert(k)
    temp=Fraction()
    for i in range(1,k):
        for j in range(1,k):
            temp1=Fraction(int(Ainv[i-1][j-1]))*Fraction(1,(k+i-1))*Fraction(1,(k+j-1))
            temp=temp+temp1
    x=Fraction(1,(2*k-1))-temp
    print("A = \n",A)
    print("xn = ",x)
    Ainv=np.linalg.inv(A)
    print("A inverse = \n", Ainv,"\n\n")