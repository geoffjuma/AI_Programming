#!/usr/bin/env python
from matplotlib import pyplot as plt 
import numpy as np 
from scipy import *

def inputs():
	x1 = input("please enter the value for percept1");
	x2 = input("please enter the value for percept2");
	return x1,x2

def innerLayer1(x1,x2):
	weight = 1
	bias = 0
	cum = x1*weight+x2*weight+bias
	if cum > 0:
		return 1
	else:
		return 0

def innerLayer2(x1,x2):
	weight = 1
	bias = -1
	cum = x1*weight+x2*weight+bias
	if cum > 0:
		return 1
	else:
		return 0
	pass
def outerLayer(cum1,cum2):
	weight1 = 3
	weight2 = -2
	bias = -2
	cum = (cum1*weight1+cum2*weight2)+bias
	if cum >0:
		return 1
	else:
		return 0

if __name__ == '__main__':
	x1,x2 = inputs()
	cum1 = innerLayer1(x1,x2)
	cum2 = innerLayer2(x1,x2)
	print outerLayer(cum1,cum2)