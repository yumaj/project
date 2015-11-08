import numpy as np
import matplotlib.pyplot as plt


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


heaplonge = (maxlong - minlong)/Interval   #how many cell 
heaplae = (maxlatitude - minlatitude)/Interval  #how many cell 


heapmap =  np.zeros((heaplonge,heaplae),float)

heaplongs = 0
heaplas = 0


###########map setting################################




for heaplongs in range(0,heaplonge):
    for heaplas in range(0,heaplae):
        heapmap[heaplongs][heaplas] = 0.0

heaplongs = 0
heaplas = 0

nc = 0




selectyear = 2010
selectmonths = 1
selectmonthe = 12


heaplongs = 0
heaplas = 0



for heaplongs in range(0,heaplonge):
    for heaplas in range(0,heaplae):
        for i  in range(len(dataset)):
            if dataset[i].pointlong <= minlong + heaplongs*Interval + Interval  and dataset[i].pointlong >= minlong + heaplongs and dataset[i].pointlatitude <= minlatitude + heaplas + Interval and dataset[i].pointlatitude >= minlatitude + heaplas:
                if dataset[i].year == selectyear and dataset[i].month <= selectmonthe and dataset[i].month >= selectmonths:
                    heapmap[heaplongs][heaplas] += 1
                    nc += 1
        
        #

print " "
for heaplongs in range(0,heaplonge):
    for heaplas in range(0,heaplae):
        print heapmap[heaplongs][heaplas],
        heapmap[heaplongs][heaplas] /= nc
    
    print " "
        



#here's our data to plot, all normal Python lists
x = [140, 141, 142, 143, 144,145]
y = [35, 36, 37, 38,39,40]
 
intensity =  np.zeros((heaplonge,heaplae),float)

for i in range(0,heaplonge):
    for j in range(0,heaplae):
        intensity[i][j] = heapmap[i][heaplae - 1 - j] 



#setup the 2D grid with Numpy
x, y = np.meshgrid(x, y)

#convert intensity (list of lists) to a numpy array for plotting
intensity = np.array(intensity)

#now just plug the data into pcolormesh, it's that easy!
plt.pcolormesh(x, y, intensity,cmap=plt.cm.Reds)
#plt.pcolor(intensity,cmap=plt.cm.Reds)
plt.colorbar() #need a colorbar to show the intensity scale
plt.show() #boom








