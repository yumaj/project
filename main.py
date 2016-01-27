import earthquakedata
import numpy as np
import random
import math
import GA
import randomf
import matplotlib.pyplot as plt
import GAwithoutUNDX
import GAwithblx

runtime = 10

GAsum = 0
Rsum = 0
GAwithoutUNDXsum = 0
GAwithBlxsum = 0

GAbest = -100000
Rbest = -100000
GAwithoutUNDXbest = -100000
GAwithBlxbest = -10000

GAarr =  np.zeros(runtime,float)
Rarr =  np.zeros(runtime,float)
GAwithoutUNDXarr = np.zeros(runtime,float)
GAwithBlxarr = np.zeros(runtime,float)

for i in range(0, runtime):
	GATEST = GA.GA()
	GAscore = GATEST.main()
	GAsum += GAscore
	if GAscore > GAbest:
		GAbest = GAscore
	GAarr[i] = GAscore

	GAwithout = GAwithoutUNDX.GA()
	GAwithoutscore = GAwithout.main()
	GAwithoutUNDXsum += GAwithoutscore
	if GAwithoutscore > GAwithoutUNDXbest:
		GAwithoutUNDXbest = GAwithoutscore
	GAwithoutUNDXarr[i] = GAwithoutscore


	R = randomf.randomf()
	Rscore = R.main()
	Rsum += Rscore
	if Rscore > Rbest:
		Rbest = Rscore
	Rarr[i] = Rscore

	BLX = GAwithblx.GA()
	GAwithblxs = BLX.main()
	GAwithBlxsum += GAwithblxs
	if GAwithblxs > GAwithBlxbest:
		GAwithBlxbest = GAwithblxs
	GAwithBlxarr[i] = GAwithblxs

GAavg = GAsum / runtime
Ravg = Rsum / runtime
GAwithoutavg = GAwithoutUNDXsum / runtime
GAwithblxavg = GAwithBlxsum / runtime

print "GAwithoutUNDXavg = " , GAwithoutavg
print "GAavg = "  ,GAavg
print "Ravg = " ,  Ravg
print "GAblxavg = ", GAwithblxavg

print "GAwithoutUNDXbest = ", GAwithoutUNDXbest
print "GAbest = ", GAbest
print "Rbest = ", Rbest
print "GABLXBEST = ", GAwithBlxbest


fig = plt.figure()
ax = fig.add_subplot(111)
labels = list('GRU1')
ax.boxplot([GAarr,Rarr,GAwithoutUNDXarr,GAwithBlxarr])
plt.show()
