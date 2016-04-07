#! /usr/bin/env python
import math

class Calculator(object):
	answer = 0
	"""docstring for ClassName"""
	def __init__(self, value1,value2,operator):
		super(Calculator, self).__init__()
		self.value1 = value1
		self.value2 = value2
		self.operator = operator

	def add(self):
		Calculator.answer = int(self.value1)+int(self.value2)
		print 'The answer is ', Calculator.answer
		return Calculator.answer
	def multiply(self):
		Calculator.answer = int(self.value1)*int(self.value2)
		print 'The answer is ', Calculator.answer
		return Calculator.answer
	def subtract(self):
		Calculator.answer = int(self.value1)-int(self.value2)
		print 'The answer is ', Calculator.answer
		return Calculator.answer
	def divide(self):
		Calculator.answer = int(self.value1)/int(self.value2)
		print 'The answer is ', Calculator.answer
		return Calculator.answer
	def square():
		Calculator.answer = int(self.value1)*int(self.value1)
		print 'The answer is ', Calculator.answer
		return Calculator.answer
	def squareroot(self):
		Calculator.answer = math.sqrt(self.value1)
		print 'The answer is ', Calculator.answer

def myInput():
	FirstValue = input('Enter the first value for calculation: \n')
	myOp = raw_input('Enter the operator: \n')
	if ((myOp == 'square')|(myOp == 'squareroot')):
		return FirstValue, myOp, FirstValue
	else:
		SecondValue = input('Enter the second value for calculation: \n')
		return FirstValue, SecondValue, myOp

if __name__ == '__main__':

	data1,data2,data3 = myInput()
	Calc = Calculator(data1,data2,data3)
	if (data3 == '+'):
		Calc.add()
	elif (data3 == '-'):
		Calc.subtract()
	elif (data3 == '*'):
		Calc.multiply()
	elif (data3 == '/'):
		Calc.divide()
	elif(data3 == 'square'):
		Calc.square()
	else:
		Calc.squareroot()