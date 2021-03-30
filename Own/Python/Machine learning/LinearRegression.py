from numpy import array, ones, zeros
from numpy.linalg import inv
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston

# Load the dataset
boston = load_boston()

X = array(boston.data[:, 5])
Y = array(boston.target)
plt.scatter(X, Y, alpha=0.2,c="green")

X = array([ones(len(X)), X]).T

B = inv(X.T@X)@X.T@Y

plt.plot([4,9],[B[0]+B[1]*4,B[0]+B[1]*9], c="red")

plt.show()