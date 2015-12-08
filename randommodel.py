import numpy as np
import matplotlib.pyplot as plt



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

############################ grenate n forecst and find  the best  one ####################################
 
n  =    100 ###set n times

best = Evalate(integerrandomforecat)

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


