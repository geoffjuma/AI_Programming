#! /usr/bin/env python
import pickle

class Address(object):
	"""docstring for Address"""
	def __init__(self, Fname, Sname, City, address, tel):
		super(Address, self).__init__()
		self.Fname = Fname
		self.Sname = Sname
		self.City = City
		self.address = address
		self.tel = tel

	def printData(self):
		print 'Your first name is: ',self.Fname
		print 'Your second name is: ',self.Sname
		print 'You live in: ',self.City
		print 'Your postal address is: ',self.address
		print 'Your telephone number is: ',self.tel

	def save(self):
		with open('adress.txt','wb') as myfile:
			pickle.dump(myaddr,myfile,-1 )

def InputData():
	Fname = raw_input('Enter your first name: \n')
	Sname = raw_input ('Enter your second name: \n')
	City = raw_input('Enter your city: \n')
	address = raw_input('Enter your adress here \n')
	tel = raw_input('Enter your telephone number here: \n')
	return Fname, Sname, City, address, tel

if __name__ == '__main__':
	param1,param2,param3,param4, param5 = InputData()
	myaddr = Address(param1,param2,param3,param4,param5)
	myaddr.save()
	myaddr.printData()