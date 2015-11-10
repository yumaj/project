import numpy as np
import matplotlib.pyplot as plt
import random
import math



class stru:
    def __init__(self):
        self.pointlong = 0
        self.pointlatitude = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.magnitude = 0
        self.depth = 0
        self.hour = 0
        self.minute = 0
        self.second = 0





f = open('data.dat','r')

dataset = [];


astr = " "

for data in open('data.dat'):
    data = stru()
    s = f.readline()
    (data.pointlong, data.pointlatitude, data.year, data.month, data.day, data.magnitude,data.depth, data.hour, data.minute, data.second) = [t(ss) for t,ss  in zip((float,float,float,float,float,float,float,float,float,float),s.split())]
    dataset.append(data)

data = stru()

dataset.append(data)

i = 0

###############map setting#############################
maxlong = 145
minlong = 140


maxlatitude = 35
minlatitude = 30

selectdata = []


i = 0


Interval = 1


heaplonge = (int)((maxlong - minlong)/Interval)   #how many cell 
heaplae = (int)((maxlatitude - minlatitude)/Interval)  #how many cell 


heapmap =  np.zeros((heaplae,heaplonge),float)

heaplongs = 0
heaplas = 0


###########map setting################################




for heaplas in range(0,heaplae):
    for heaplongs in range(0,heaplonge):
        heapmap[heaplas][heaplongs] = 0.0

heaplongs = 0
heaplas = 0

nc = 0




selectyear = 2010
selectmonths = 1
selectmonthe = 12


heaplongs = 0
heaplas = 0


print "hdaoplinge  = " , heaplonge


for heaplas in range(0,heaplae):
    for heaplongs in range(0,heaplonge):
        for i  in range(len(dataset)):
            if dataset[i].pointlong <= minlong + heaplongs*Interval + Interval  and dataset[i].pointlong >= minlong + heaplongs*Interval and dataset[i].pointlatitude <= minlatitude + heaplas*Interval + Interval and dataset[i].pointlatitude >= minlatitude + heaplas*Interval:
                if dataset[i].year == selectyear and dataset[i].month <= selectmonthe and dataset[i].month >= selectmonths:
                    heapmap[heaplas][heaplongs] += 1
                    nc += 1
        
        #

print " "

print "c = " , nc


print "happen times"

for i in range(0,heaplae):
    for j in range(0,heaplonge):
        print heapmap[i][j],
    
    print " "
        

for i in range(0,heaplae):
    for j in range(0,heaplonge):
        heapmap[i][j] /= nc
        print heapmap[i][j],
    
    print " "
        

print " "

print "happen/happen sum : "

for i in range(0, heaplae):
    for j in range(0,heaplonge):
        print heapmap[heaplae - 1 - i][j],

    print " "


print " "
#here's our data to plot, all normal Python lists






################### random forecast###########################


randomforecat = np.zeros((heaplae , heaplonge ),float)


########## generate the uniform balue between 0 and 1 each vin 1###################
for i in range(0,heaplae):
    for j in range(0,heaplonge):
        randomforecat[i][j] = random.uniform(0, 1)


##################################################################

print "randomforecat :"
for i in range(0,heaplae):
    for j in range(0, heaplonge):
        print randomforecat[i][j],
    print " "



################# algorithm 1####################################

def algo1(x, mu):
    L = math.exp(-1 * mu)
    k = 0
    prob = 1

    while prob < L:
        k += 1
        prob = prob * x

    return k

###############################################################


#####################Transform ###############################


integerrandomforecat = np.zeros((heaplae , heaplonge ),float)

for i in range(0,heaplae):
    for j in range(0,heaplonge):
        
        integerrandomforecat[i][j] = algo1(randomforecat[i][j], heapmap[i][j])

##########################################################

print "integerrandomforecat : "

for i in range(0,heaplae):
    for j in range(0, heaplonge):
        print integerrandomforecat[i][j],
    print " "










############################print heapmap####################
x =  np.zeros((heaplonge + 1),float)
y =  np.zeros((heaplae + 1),float)

for i in range(0,heaplonge + 1): x[i] = minlong + i * Interval
for i in range(0,heaplae + 1): y[i] = minlatitude + i * Interval

intensity =  np.zeros((heaplae,heaplonge),float)

for i in range(0, heaplae):
    for j in range(0,heaplonge):
        intensity[i][j] = heapmap[heaplae - 1 - i][j] 




#setup the 2D grid with Numpy
x, y = np.meshgrid(x, y)

#convert intensity (list of lists) to a numpy array for plotting
intensity = np.array(intensity)

#now just plug the data into pcolormesh, it's that easy!
plt.pcolormesh(x, y, intensity,cmap=plt.cm.Reds)
#plt.pcolor(intensity,cmap=plt.cm.Reds)
plt.colorbar() #need a colorbar to show the intensity scale
plt.show() #boom




############################print heapmap####################








