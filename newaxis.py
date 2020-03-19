#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://medium.com/@ian.dzindo01/what-is-numpy-newaxis-and-when-to-use-it-8cb61c7ed6ae
"""

arr = np.arange(4)
print(arr)
print(arr.shape)
row_vec = arr[np.newaxis, :]
print(row_vec)
print(row_vec.shape)

col_vec = arr[:, np.newaxis]
print(col_vec)
print(col_vec.shape)