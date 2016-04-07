

#!/usr/bin/env python
import numpy as np 
import math
import matplotlib.pyplot as plt 
def CosSine(num, num ):
	t = np.linspace(-2*(np.pi), 2*(np.pi), 256,endpoint=True)
	#for x in t:
		#print x
	x,y = np.cos(t),np.sin(t);
	plt.plot (t,x, )
	plt.plot (t,y, color ="red", linewidth = 1.0, linestyle = "-")
	plt.show()
CosSine()


