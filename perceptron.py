#!/usr/bin/env python

"single layer perceptron network with sigmoid activation function"
import numpy as np 
from matplotlib import pyplot as plt 

def sigmoid(x,deriv=False):
	if (deriv ==True):
		return x*(1-x);
	else:
		return 1/(1+np.exp(-x))

def inputVector():
	x = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
	return x;

def ouputVector():
	y = np.array([[0,1,1,0]]).T
	return y

def learning(x,y):
	beta = 0.01;
	w = 2*np.random.random((3,1))-1;
	for i in range (1000):
		pred = sigmoid(np.dot(x,w));
		error = beta*(np.dot(x.T,y-pred))
		w = w+error
	return pred;

if __name__ == '__main__':
	x = inputVector();
	y = ouputVector();
	 
	print np.round(learning(x,y))
	x_axis = np.linspace(-10,10,50)
	plt.plot(x_axis,sigmoid(x_axis))
	plt.xlabel('x axis')
	plt.ylabel('1/1+exp(-1)')
	plt.show()
