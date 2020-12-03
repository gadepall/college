import numpy as np

E=np.array([[1-1j,-2,3-3j,-6],[3,-1-1j,9,-3-3j],[7-7j,-14,-2+2j,4],[21,-7-7j,-6,2+2j]])

A=np.array([[1-1j,-2],[3,-1-1j]])
B=np.array([[3-3j,-6],[9,-3-3j]])
C=np.array([[7-7j,-14],[21,-7-7j]])
D=np.array([[-2+2j,4],[-6,2+2j]])

detE=np.linalg.det(E)

K=np.matmul(A,D)-np.matmul(B,C)

detK=np.linalg.det(K)

print(detE)
print(detK)
