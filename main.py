import earthquakedata
import numpy as np
import random
import math
import GA
import randomf
import matplotlib.pyplot as plt


runtime = 10
GAsum = 0
Rsum = 0
GAbest = -100000
Rbest = -100000
GAarr =  np.zeros(runtime,float)
Rarr =  np.zeros(runtime,float)


for i in range(0, runtime):
	GATEST = GA.GA()
	GAscore = GATEST.main()
	GAsum += GAscore
	if GAscore > GAbest:
		GAbest = GAscore
	GAarr[i] = GAscore

	R = randomf.randomf()
	Rscore = R.main()
	Rsum += Rscore
	if Rscore > Rbest:
		Rbest = Rscore
	Rarr[i] = Rscore

GAavg = GAsum / runtime
Ravg = Rsum / runtime

print "GAavg = "  ,GAavg
print "Ravg = " ,  Ravg
print "GAbest = ", GAbest
print "Rbest = ", Rbest

fig = plt.figure()
ax = fig.add_subplot(111)

ax.boxplot([GAarr,Rarr])
plt.show()
