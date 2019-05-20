#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:20:09 2019

@author: derekcortez
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x=[1,5,1.5,8,1,9]
y=[1,8,1.8,8,0.6,11]

#Scatter
plt.scatter(x,y)
plt.show()