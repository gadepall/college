from sympy import *
import cmath

x=0
y=-1
x1=0
y1=1
x2=1
y2=1
z=complex(x,y)
z1=complex(x1,y1)
z2=complex(x2,y2)

A = Matrix([[1,z],[2,2],[z1,z2]])
print("Matrix A is",A)
print("Row-Reduced form and pivot elements are",A.rref())
