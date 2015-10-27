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




maxlong = 145
minlong = 140


maxlatitude = 35
minlatitude = 30

selectdata = []

i = 0

heapmap =  np.zeros((5,5),float)

heaplongs = 0
heaplas = 0

heaplonge = 5
heaplae = 5

for heaplongs in range(heaplonge):
    for heaplas in range(heaplae):
        heapmap[heaplongs][heaplas] = 0.0

heaplongs = 0
heaplas = 0

nc = 0


Interval = 1

selectyear = 2010
selectmonths = 1
selectmonthe = 12


heaplongs = 0
heaplas = 0



for heaplongs in range(heaplonge):
    for heaplas in range(heaplae):
        for i  in range(len(dataset)):
            if dataset[i].pointlong <= minlong + heaplongs + Interval  and dataset[i].pointlong >= minlong + heaplongs and dataset[i].pointlatitude <= minlatitude + heaplas + Interval and dataset[i].pointlatitude >= minlatitude + heaplas:
                if dataset[i].year == selectyear and dataset[i].month <= selectmonthe and dataset[i].month >= selectmonths:
                    heapmap[heaplongs][heaplas] += dataset[i].magnitude
                    nc += 1
        if nc == 0 : nc = 1
        print heapmap[heaplongs][heaplas],
        heapmap[heaplongs][heaplas] /= nc
        #heapmap[heaplongs][heaplas] /= 10
        nc = 0
    print " "




heaplongs = 0
heaplas = 0

for heaplongs in range(heaplonge):
    for heaplas in range(heaplae):
        print heapmap[heaplongs][heaplas],
    
    print " "
        
print " "
print nc
print s


#here's our data to plot, all normal Python lists
x = [140, 141, 142, 143, 144,145]
y = [35, 36, 37, 38,39,40]

intensity = [
    [heapmap[0][4], heapmap[1][4], heapmap[2][4], heapmap[2][4], heapmap[2][4]],
    [heapmap[0][3], heapmap[1][3], heapmap[2][3], heapmap[2][3], heapmap[2][3]],
    [heapmap[0][2], heapmap[1][2], heapmap[2][2], heapmap[2][2], heapmap[2][2]],
    [heapmap[0][1], heapmap[1][1], heapmap[2][1], heapmap[2][1], heapmap[2][1]],
    [heapmap[0][0], heapmap[1][0], heapmap[2][0], heapmap[2][0], heapmap[2][0]]
]

#setup the 2D grid with Numpy
x, y = np.meshgrid(x, y)

#convert intensity (list of lists) to a numpy array for plotting
intensity = np.array(intensity)

#now just plug the data into pcolormesh, it's that easy!
plt.pcolormesh(x, y, intensity,cmap=plt.cm.Reds)
#plt.pcolor(intensity,cmap=plt.cm.Reds)
plt.colorbar() #need a colorbar to show the intensity scale
plt.show() #boom








