#!/usr/bin/env python
# coding: utf-8

# In[14]:


#! /usr/bin/python3
# Example to prove a mxn matrix A, can be written as R = PAQ where R is in both row reduced
# and column reduced matrix form. Also P and Q are invertible.
import numpy as np

# Here we take a 2x4 matrix, perform elementary operarions on that matrix and finally show
# that it can be written in both row reduced and column reduced matrix form

A = np.array([[1,5,6,2],
             [2,12,7,5]], dtype=float) 

# A can be transformed to row reduced echelon form by multiplying with matrix P (Sequence 
#of elementary row operations)
P = np.array([[6, -2.5],
             [-1, 0.5]], dtype=float)

# The following matrix R_1 is in row reduced echelon form
R_1 = np.dot(P,A)

# Further R_1 can be transformed into column reduced echelon form by multilpying with
# matrix Q(Sequence of elementary column operations)
Q = np.array([[1,0,-18.5,0.5],
             [0,1,2.5,-0.5],
             [0,0,1,0],
             [0,0,0,1]], dtype=float)

# The following matrix R is in both row-reduced and column-reduced echelon form
R = np.dot(R_1,Q)
print("The row and column reduced matrix of A is")
print(R)
# where R = (R_1)Q = PAQ

# Proving P is an invertible
try:
    P_inv = np.linalg.inv(P)
    print("Inverse exists for P which has dimensions:",np.shape(P))
    print("P Inverse: ")
    print(P_inv)
except LinAlgError:
    print("Inverse does not exist for P")

# Proving Q is an invertible
try:
    Q_inv = np.linalg.inv(Q)
    print("Inverse exists for Q which has dimensions:",np.shape(Q))
    print("Q Inverse: ")
    print(Q_inv)
except LinAlgError:
    print("Inverse does not exist for Q")

