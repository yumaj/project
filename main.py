import numpy as np
import matplotlib.pyplot as plt
import random
import math
import earthquakedata



data = earthquakedata.dataremodel()


path = 'data.dat'



###############map setting#############################



data.longitudemax = 145
data.longitudemin = 140


data.latitudemax = 35
data.latitudemin = 30

data.Interval = 1

data.datareader(path)
###########################################

data.selectyear = 2010
data.selectmonths = 1
data.selectmonthe = 12

data.setnum()



data.findhappentimes()



data.setmodel()


print " "

print "c = " , data.nc

#here's our data to plot, all normal Python lists


data.printmap()


################### random forecast###########################


randomforecat = np.zeros((data.latitudenum , data.longitudebinnum ),float)


########## generate the uniform balue between 0 and 1 each vin 1###################
for i in range(0,data.latitudenum):
    for j in range(0,data.longitudebinnum):
        randomforecat[i][j] = random.uniform(0, 1)


##################################################################

print "randomforecat :"
for i in range(0,data.latitudenum):
    for j in range(0, data.longitudebinnum):
        print randomforecat[i][j],
    print " "



################# algorithm 1####################################

def algo1(x, mu):       ##############from Claus  teacher's  invertPoisson fuction
   if(mu >= 0):
        if(x >= 0):
            if(x < 1):
                l = math.exp(-mu)
                k = 1
                prob = 1 * x
                while(prob>l):
                    k += 1
                    prob = prob * x
                return k

###############################################################


#####################Transform ###############################


integerrandomforecat = np.zeros((data.latitudenum , data.longitudebinnum ),float)

for i in range(0,data.latitudenum):
    for j in range(0,data.longitudebinnum):
        
        integerrandomforecat[i][j] = algo1(randomforecat[i][j], data.dataremodel[i][j])

##########################################################

print "integerrandomforecat : "

for i in range(0,data.latitudenum):
    for j in range(0, data.longitudebinnum):
        print integerrandomforecat[i][j],
    print " "





################# simple Log Likelihood  #########################



def Likelihood(testintegerrandomforecat):
    Likelihood = 0

    for i in range(0,data.latitudenum):
        for j in range(0,data.longitudebinnum):##
            Likelihood += (-testintegerrandomforecat[i][j] + data.dataremodel[i][j] * math.log(testintegerrandomforecat[i][j]) - math.log(testintegerrandomforecat[i][j]))    ####had problem 

    return Likelihood



######################################################################

############################ grenate n forecst and find  the best  one ####################################


n  =    100 ###set n times

best = Likelihood(integerrandomforecat)

bestrandomforecat = np.zeros((data.latitudenum , data.longitudebinnum ),float)

print "the first = ",best, " "


for i in range(0, data.latitudenum):  ######## set the first is the best
    for j in range(0,data.longitudebinnum):
        bestrandomforecat[i][j] = randomforecat[i][j]


for r in range(0, n):

    for i in range(0,data.latitudenum):###gerante
        for j in range(0,data.longitudebinnum):
            randomforecat[i][j] = random.uniform(0, 1)

    for i in range(0,data.latitudenum):#####transfer
        for j in range(0,data.longitudebinnum):

            integerrandomforecat[i][j] = algo1(randomforecat[i][j], data.dataremodel[i][j])

    rLikelihood = Likelihood(integerrandomforecat)

    if(rLikelihood >  best):
        for i in range(0, data.latitudenum):  ######## set the map 
            for j in range(0,data.longitudebinnum):
                bestrandomforecat[i][j] = randomforecat[i][j]

        best = rLikelihood
    print "the ", r,  " times = " , rLikelihood



print "the best = " , best




#######################################################################


