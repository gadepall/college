from sympy import *
import cmath
x=0
y=1
x1=-1
y1=-1
x2=0
y2=2
z=complex(x,y)
z1=complex(x1,y1)
z2=complex(x1,y1)

A = Matrix([[z,z1,0],[1,-2,1],[0,z2,-1]])
print("Matrix A is",A)

print("Row-Reduced form and pivot elements are",A.rref())
