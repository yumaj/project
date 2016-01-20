import numpy as np
import random


def BLX(P1,P2,C ,sizex, sizey):
	alpha = 0.4
	for i in range(0, sizex):
		for j in range(0, sizey):
			dx = np.absolute(P1[i][j] - P2[i][j])
			if P1[i][j] > P2[i][j] :
				minx = P2[i][j]
			else :
				minx = P1[i][j]
			if P1[i][j] > P2[i][j] :
				maxx = P1[i][j]
			else : 
				maxx = P2[i][j]
			mincx = minx - alpha * dx
			maxcx = maxx + alpha * dx
			C[i][j] = random.uniform(mincx,maxcx)

