#! /usr/bin/env python
class Employee(object):
	"""docstring for Employee"""
	employeeCount = 0
	def __init__(self, name,ssnum,salary,dob):
		super(Employee, self).__init__()
		self.name = name
		self.ssnum = ssnum
		self.salary = salary 
		self.dob = dob
		Employee.employeeCount +=1
	def printDetails(self):
		print "my name is ", self.name
		print "I am "+self.dob+" old"
		print "The government social security is ",self.ssnum
		print "I am being paid "+self.salary+" Kshs"
		print "Thank you very much!!!"
	def printCount(self):
		print "the number of employees is ", Employee.employeeCount
	def calCulater(self):
		print "The total number of employees here %d ", Employee.employeeCount
		"""instantiating the classes ie creating the objects"""

employee1 = Employee('Juma','123456','40000','11/01/196')
employee1.printDetails()
employee1.printCount()