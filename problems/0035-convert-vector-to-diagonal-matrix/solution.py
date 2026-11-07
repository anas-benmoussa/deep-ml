import numpy as np

def make_diagonal(x):
	mat=np.zeros((len(x),len(x)))
	for i in range(len(x)):
		mat[i,i]=x[i]
	return mat