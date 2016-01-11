import numpy as np
import random
import collections


def UNDX(P1, P2, P3, C1, C2,sizex,sizey):

	d1 = 0
	d2 = 0
	alpha = 0.5
	beta = 0.35/np.sqrt(sizex * sizey)

	r = random.uniform(0,alpha * alpha)
	ni = random.uniform(0,beta * beta)

	for i in range(0,sizex):
		for j in range(0, sizey):
			p = (P1[i][j] + P2[i][j])/2
			d = P2[i][j] - P1[i][j]
			P3_P1 = (P3[i][j] - P1[i][j])*(P3[i][j] - P1[i][j])
			D = np.sqrt(P3_P1 - ((d*P3_P1)*(d*P3_P1))/(d*d))

			C1[i][j] = p + (r * d) + D*(ni * (P3[i][j] - P2[i][j])/np.absolute(P3[i][j] - P2[i][j]) )
			C2[i][j] = p - (r * d) - D*(ni * (P3[i][j] - P2[i][j])/np.absolute(P3[i][j] - P2[i][j]) )
	


