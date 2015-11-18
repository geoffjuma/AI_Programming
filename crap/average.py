#! /usr/bin/env python
values  = [];

def myinput():
	data = input('How many numbers do you want to enter: ')
	n = 0;
	while n < data:
		values[n] = values.append(input('Enter the values to be calculated: '));
		n +=1;
	return values,data;

def calculator(numbers, times):
	n = 0;
	average = 0.0;
	while n < times:
		average = sum(numbers[n])/n;
	print 'The average is: ', average; 

myvalues,mytimes = myinput()
calculator(myvalues, mytimes)

