
import numpy as np
A = np.array([[2, -1, 1],
             [1, 2, 1]]) 

# a 2x3 matrix
B = np.array([[3],
             [1],
             [-1]])
C = np.array([[1, -1]]) 

AB = np.dot(A, B)

ABC= np.dot(AB,C)

print("MULTIPLICATION of A and B:\n{} shape={}".format(AB, AB.shape))
print("MULTIPLICATION of AB and C:\n{} shape={}".format(ABC, ABC.shape))


CAB = np.dot(C,AB)
print("MULTIPLICATION of C and AB:\n{} shape={}".format(CAB, CAB.shape))
 