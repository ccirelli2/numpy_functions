#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Documentation:
    Url https://machinelearningmastery.com/introduction-to-expected-value-variance-and-covariance/
    
"""


# Import Packages
import numpy as np

# Create An Array & Get Mean
v = np.array([1,2,3,4,5,6])

# Create 2D Array & Get Mean
M = np.array([[1,2,3,4,5], [1,2,3,4,5]])
col_mean = np.mean(M, axis=0)
row_mean = np.mean(M, axis=1)

# Get Variance (ddof stands for degrees of freedom)
v_var = np.var(v, ddof=0)
v_std = np.std(v)

# Covariance
x = np.array([1,2,3,4,5])
y = np.array([5,4,3,2,1])
'''access just the covariance for the two variables as the 
   [0,1] element of the square covariance matrix returned'''
v_cov = np.cov(x,y)[0,1]

# Correlation (divide by std)
corr = np.corrcoef(x,y)[0,1]

# Covariance matrix 
'''
    Diagonal of the covariance matrix are the variances
    and the other entries are the covariances. 
    
    For two dimensions:  C = (sigma(x,x) sigma(x,y)
                              sigma(y,x) sigma(y,y))
'''

cov_m = np.cov(x,y)
print(cov_m)

# Create 3d cov matrix
z = [5,6,7,8,9]
cov_m3 = np.cov(x,y,z)
print(cov_m3)s


print('Mean => {}'.format(np.mean(v)))
print('Var  => {}'.format(v_var))
print('Std  => {}'.format(v_std))
print('Cov  => {}'.format(v_cov))
print('Corr => {}'.format(corr))