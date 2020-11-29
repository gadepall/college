import numpy as np
import scipy.linalg as la
J=np.array([[0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,1,0,0],
            [0,0,0,0,1,0,0],
            [0,0,0,0,0,1,1],
            [0,0,0,0,0,0,1]])
J1=np.array([[0,1,0],[0,0,0],[0,0,0]]) 
J2=np.array([[1,1,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]]) 

A1=np.matmul(J,J)
rank1=np.linalg.matrix_rank(A1)
print('Nullity of J^2:',7-rank1)
A2=np.matmul(J-np.eye(7),J-np.eye(7))
rank2=np.linalg.matrix_rank(A2)
print('Nullity of (J-I)^2:',7-rank2)
Vb1=la.null_space(A1)
Vb2=la.null_space(A2)
print('Basis for V1:\n',Vb1)
print('Basis for V2:\n',Vb2)
#print('T^2(T-I)^2:\n',np.matmul(A1,A2))
#print('T(T-I)^2:\n',np.matmul(J,A2))
