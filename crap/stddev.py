#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt  


def getValues():
	num = []
	for y in range(10):
		x = input("enter some numbers: ");
		num.append(x);
	return num
def getDeviation(num):
	mysum = 0.0
	for i in range(len(num)):
		mysum += num[i]
	mean = mysum/10.0;
	return mysum, mean
def getVariance(num, mean):
	x = len(num)
	differences = [];
	sumdiff = 0;
	for i in range (x):
		diff = num[i]-mean
		differences.append(diff)	
		diffsquared = diff**2
		sumdiff +=diffsquared; 
		return differences
	variance = sumdiff/x
	print"the variance from the mean ", differences
	print "the variance is :", variance
		#variance.append(diff) 

values = getValues()
sumx,meanx = getDeviation(values)
thediff = getVariance(values,meanx)
#draw();

## printing the different values
print values
print "the totat sum: " ,sumx
print "the mean of the number is :" ,meanx
## Ploting the graph for the values

for i in range(len(values)):
	for j in range(len(thediff)):
		plt.plot(values[i],thediff[j],'*')
plt.xlabel("i = values enter")
plt.ylabel("j = variance")
plt.show();