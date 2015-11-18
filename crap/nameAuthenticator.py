#!/ usr/bin/env python
name = 'juma'
def authenticator(theguess):
	count = 2
	while count>0:
		if theguess == name:
			print "Yes! I am ",theguess
			marks = getMarks(theguess)
			break;
		else:
			print "No!, I am not ",theguess
			print "you have ",count,"more attempt remaining!"
			theguess = userInpput()
		count-=1
		
def getMarks(guess):
	mark = input("Please enter your marks: ")
	if (mark >80):
		print "You are an excellent Student"
	elif (mark >=70 and mark<=80):
		print "You are a good student"
	elif (mark >=60 and mark<70):
		print "You are a fair student"
	elif (mark>=50 and mark<60):
		print "you are poor student"
	else:
		print "You have failed"

def userInpput():
	guess = raw_input("Guess who I am ??! ");
	return guess

theguess = userInpput()
authenticator(theguess)