import urllib
import urllib2
def getURL():
	urlcontents = urllib.urlopen('http://www.nation.co.ke/')
	html = urlcontents.read()
	#print html
	links = html.find('<a href = ')
	if (links == -1):
		print 'end of file'
	else:
		href = html.find('"',links+1)
		endOfHref = html.find('"'.href+1)
	closeTag = html.find("</a>",links)

	print links

getURL()