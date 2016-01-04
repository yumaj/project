import numpy as np
import random
import collections

def ch(arra, arrb, sizex, sizey):
	for i in range(0, sizex):
		for j in range(0, sizey):
			if arra[i][j] != arrb[i][j] :
				return 1 
		if i == sizex -1 :
			return -1

def UNDX(P1, P2, P3, C1, C2,sizex,sizey):

	d1 = 0
	d2 = 0
	alpha = 0.5
	beta = 0.35
	P1e1 = 0
	
	P3e1 = 0

	z2e1 = 0

	if 	ch(P1,P2,sizex,sizey) == -1 :
		return False
	middle = np.zeros((sizex ,sizey ),float)

	for i in range(0,sizex):
		for j in range(0,sizey):
			middle[i][j] = (P1[i][j] + P2[i][j])/2

	diffP1_P2 = np.zeros((sizex ,sizey ),float)

	for i in range(0,sizex):
		for j in range(0,sizey):
			diffP1_P2[i][j] = P1[i][j] - P2[i][j]
			d1 += diffP1_P2[i][j] * diffP1_P2[i][j]


	D1 = np.sqrt(d1)

	delta1 = alpha * D1
	
	z1 = random.uniform(0,delta1 * delta1)

	e1 = np.zeros((sizex ,sizey ),float)

	for i in range(0,sizex):
		for j in range(0, sizey):
			e1[i][j] = - diffP1_P2[i][j] / D1

	for i in range(0, sizex):
		for j in range(0,sizey):
			P1e1 += P1[i][j] * e1[i][j]

			P3e1 += P3[i][j] * e1[i][j]


	s = -1 * P1e1 + P3e1

	Q = np.zeros((sizex ,sizey ),float)


	for i in range(0, sizex):
		for j in range(0, sizey):
			Q[i][j] = P1[i][j] + s * e1[i][j]

	diffP3_Q = np.zeros((sizex ,sizey ),float)

	for i in range(0 , sizex):
		for j in range(0, sizey):
			diffP3_Q[i][j] = Q[i][j] - P3[i][j]
			d2 += diffP3_Q[i][j] * diffP3_Q[i][j]

	D2 = np.sqrt(d2)

	delta2 = beta * D2 / np.sqrt(sizex * sizey)
	z2 = np.zeros((sizex ,sizey ),float)

	for i in range(0, sizex):
		for j in range(0,sizey):
			z2[i][j] = random.uniform(0,delta1 * delta1)

	for i in range(0, sizex):
		for j in range(0, sizey):
			z2e1 += z2[i][j] * e1[i][j]

	for i in range(0, sizex):
		for j in range(0 , sizey):
			z2[i][j] = z2[i][j] - z2e1 * e1[i][j]

	for i in range(0, sizex):
		for j in range(0, sizey):
			z2[i][j] = z2[i][j] + z1 * e1[i][j]


	for i in range(0, sizex):
		for j in range(0 , sizey):
			newC1 = middle[i][j] + z2[i][j]
			newC2 = middle[i][j] - z2[i][j]
			if newC1 > 0 and newC1 < 1 :
				C1[i][j] = middle[i][j] + z2[i][j]
			if newC2 > 0 and newC2 < 1:
				C2[i][j] = middle[i][j] - z2[i][j]




