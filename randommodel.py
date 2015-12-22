import numpy as np
import matplotlib.pyplot as plt
import random
import math




def printrandomforecat(self,model): ## need fix 
    print "randomforecat :"
    for i in range(0,model.latitudenum):
        for j in range(0, model.longitudebinnum):
            print model[i][j],
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


################################################
def generatemodel(latitudenum,longitudebinnum):

    randomforecat = np.zeros((latitudenum ,longitudebinnum ),float)

    for i in range(0,latitudenum):###gerante
        for j in range(0,longitudebinnum):
            randomforecat[i][j] = random.uniform(0, 1)

    return randomforecat

################################################

def intergermodel(model,latitudenum,longitudebinnum):
    
    integerrandomforecat = np.zeros((latitudenum ,longitudebinnum ),float)

    for i in range(0,latitudenum):#####Transform
        for j in range(0,longitudebinnum):
            integerrandomforecat[i][j] = algo1(model[i][j],model[i][j])

    return integerrandomforecat



