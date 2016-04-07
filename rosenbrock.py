#!/usr/bin/env python

from scipy import optimize as opt 
from scipy.integrate import odeint
import numpy as np 
from matplotlib import pyplot as plt 
from sympy import *
import math
#plt.style.use('ggplot')

x = Symbol('x')

def f(x):
	return x**4 + 3*(x-2)**3 - 15*(x)**2 + 1
	
def derivative(f,yo,x0):
	d = odeint(f,y0,x)
	pass
if __name__ == '__main__':
	x0 = np.linspace(-8,8,100);
	y0 = 0;
	#d = derivative(f,y0,x0)
	#plt.plot(x0,f(x0),x0,d[:,0])
	plt.plot(x0,f(x0))
	plt.show()