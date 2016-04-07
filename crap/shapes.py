#! usr/bin/env python

class Shapes(object):
	area = 0
	perimeter = 0
	"""dlength, widthtring for Shapes"""
	def __init__(self, length, width):
		super(Shapes, self).__init__()
		""" Defining the attributes of the class """
		self.length = length
		self.width = width
	"""Defining the functions to manipulate the attributes above"""
	def calculateArea(self):
		Shapes.area = int (self.length)*int(self.width)
		return Shapes.area
	def calculatePerimeter(self):
		if int (self.length) == int (self.width):
			Shapes.perimeter = 4*int (self.length)
			print 'This is a square'
		else:
			Shapes.perimeter = 2*(int(self.length)+int(self.width))
			print 'This is a rectangle'
		return Shapes.perimeter
	def displayResults(self):
		print 'You have entered ', self.width,self.length
		print 'The Area of this shape is ', Shapes.area
		print 'The perimeter of this shape is ', Shapes.perimeter
	
def inputParameters():
	input1 = input('Enter the length of the shape: ')
	input2 = input('Enter the width of the shape: ')
	return input1, input2

param1, param2 = inputParameters()
	
object1 = Shapes(param1,param2)
object1.calculatePerimeter()
object1.calculateArea()
object1.displayResults()