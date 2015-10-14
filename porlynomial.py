#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt 
def plotCurve():
	x  = [32,64,96,118,126,144,152.5,158]  
	y = [99.5,104.8,108.5,100,86,64,35.3,15]
	plt.scatter (x,y,marker = 'o',color = 'blue');

	# create nth degree polynomial fit
	n = 1
	zn = polyfit(x,y,n) 
	pn = poly1d(zn) # construct polynomial

	
	plt.plot(x, pn(x),'r')
	
	plt.xlabel('The x axis');
	plt.ylabel('The y axis');
	plt.title('Some funny curve data');
	plt.show();

if __name__ == '__main__':
	plotCurve()
