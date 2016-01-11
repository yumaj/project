import earthquakedata
import randommodel
import numpy as np
import math
import random
import GA
import UNDX
import randomf

Population_size = 50
Tournament_size = 50
Generation = 100
Crossover_Chance = 0.9
Mutation_Chance_individual = 0.8

longitudemax = 145
longitudemin = 140
latitudemax = 35
latitudemin = 30
Interval = 1

longitudebinnum = (int)((longitudemax - longitudemin)/Interval)   #how many bins 
latitudenum = (int)((latitudemax - latitudemin)/Interval)  #how many bins 	




######### loop ########################    
best = -100000
data = earthquakedata.dataremodel()


path = 'data.dat'

######## map setting #######

data.longitudemax = 145
data.longitudemin = 140


data.latitudemax = 35
data.latitudemin = 30

data.Interval = 1

data.datareader(path)

######## setting end ######

data.selectyear = 2010
data.selectmonths = 1
data.selectmonthe = 12

data.setnum()

data.findhappentimes()



data.setmodel()
GAf = GA.GA()
newP = []
Rsum = 0
R = randomf.randomf()
Rscore = R.main()
Rsum += Rscore
if Rscore > Rbest:
	Rbest = Rscore
