import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Dataset
N = 1000
X = np.random.random((N, 2)) * 6 - 3
Y = np.cos(2*X[:,0]) + np.cos(3*X[:,1])

# this represents the function: y = cos(2X1) + cos(3X2)

#plot it

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
print('put a debugger here to stop the plot to disappear')