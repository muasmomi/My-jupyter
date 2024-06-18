# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:05:31 2022

@author: ACER
"""
import matplotlib.pyplot as plt
from math import*
import numpy as np
xo=float(input("Enter initial guess: "))
def function_1(x):
    return (2*x**2-1)*np.exp(-x*2)
def function_2(x):
    return 2*x*(3-2*x**2)*np.exp(-x*2)
dx=1
while dx>1e-10:
    x1=xo-(function_1(xo))/(function_2(xo))
    print(x1)
    dx=abs(x1-xo)
    xo=x1
print("done loop")
fx1= 0.5-x1*np.exp(-x1**2)
print(fx1)