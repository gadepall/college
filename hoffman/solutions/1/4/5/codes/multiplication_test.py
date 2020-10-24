import numpy as np

c1=int(input('Enter any value='))
c2=int(input('Enter any value='))
M= np.array([[1,1,0],[-4,0,0]])
P = c1*np.array([[-1/2,-1/4,1],[0,0,0]])
print('P=',P)
Q = c2*np.array([[0,0,0],[-1/2,-1/4,1]])
print('Q=',Q)
C=M+P+Q
print('C=',C)
A= np.array([[1,-1],[2,2],[1,0]])
B= np.array([[3,1],[-4,4]])

Y= np.matmul(C,A)
print('CA=',Y)

if (Y==B).any():
	print('CA=B is satisfied')
else:
	print('Not matched')

