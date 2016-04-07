#! /usr/bin/env python

def max():
	array = [-20, 19, 1, 5, -1, 27, 19, 5];
	max = array[0];
	i = 0;
	while i< len(array):
		if (array[i]>max):
			max  = array[i];
		i+=1;
	print 'The maximum element is: ', max;
max()