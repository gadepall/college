#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:12:29 2020

@author: shantanu
"""

import numpy as np

A=np.array([[1,2,3,4],[0,2,3,4],[0,0,3,4],[0,0,0,4]])
Ainv=np.linalg.inv(A)
I=A@Ainv
print(A)
print(Ainv)
print(I)