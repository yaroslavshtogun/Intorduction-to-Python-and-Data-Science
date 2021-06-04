# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:31:47 2021

@author: 4471082
"""

# Load labraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Plot for 200 random points
rng = np.random.RandomState(1)

plt.figure(figsize = (5,5))  # Set Figure size 

X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axis('equal')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)

print(pca.components_)

print(pca.explained_variance_)

def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# plot data
plt.figure(figsize = (5,5))  # Set Figure size 
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v)
plt.axis('equal')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()