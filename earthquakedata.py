import numpy as np
import matplotlib.pyplot as plt



class data_stru:

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
        

      


class dataremodel:

    def __init__(self):

        self.dataset = []
        self.Interval = 0
        self.longitudemax = 0
        self.longitudemin = 0
        self.latitudemax = 0
        self.latitudemin = 0
        self.longitudebinnum = 0
        self.latitudenum = 0
        self.dataremodel = []
        self.selectyear = 0
        self.selectmonths = 0
        self.selectmonthe = 0
        self.nc = 0.0
        self.score = 0.0


    def setnum(self):

        self.longitudebinnum = (int)((self.longitudemax - self.longitudemin)/self.Interval)   #how many bins 
        self.latitudenum = (int)((self.latitudemax - self.latitudemin)/self.Interval)  #how many bins 

        self.dataremodel =  np.zeros((self.latitudenum,self.longitudebinnum),float)
        self.nc = 0

        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):
                self.dataremodel[i][j] = 0.0
            



    def datareader(self,path):
        inputself = open(path,'r')

        for filen in open(path):

            data = data_stru()
            
            s = inputself.readline()  #### read a self
            
            (data.pointlong, data.pointlatitude, data.year, data.month, data.day, data.magnitude,data.depth, data.hour, data.minute, data.second) = [t(ss) for t,ss  in zip((float,float,float,float,float,float,float,float,float,float),s.split())] ##transfer to selfstruct

            self.dataset.append(data)  ##### put self in to dataset
        #print len(self.dataset)
            #print self.year

    def findhappentimes(self):    

        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):
                for k  in range(0,len(self.dataset)):
                    if self.dataset[k].pointlong <= self.longitudemin + j * self.Interval + self.Interval  and self.dataset[k].pointlong >= self.longitudemin + j*self.Interval and self.dataset[k].pointlatitude <= self.latitudemin + i*self.Interval + self.Interval and self.dataset[k].pointlatitude >= self.latitudemin + i*self.Interval:
                        
                        if self.dataset[k].year == self.selectyear and self.dataset[k].month <= self.selectmonthe and self.dataset[k].month >= self.selectmonths:
                            self.dataremodel[i][j] += 1
                            self.nc += 1  ##earthquake happen time + 1
                            
                            
    def setmodel(self):
        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):
                self.dataremodel[i][j] /= self.nc


    def printmodel(self):
        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):
                print self.dataremodel[i][j],
    
            print " "
                    

        print " "


    def printmap(self):

        print "happen/happen sum : "

        for i in range(0, self.latitudenum):
            for j in range(0,self.longitudebinnum):
                print self.dataremodel[self.latitudenum - 1 - i][j],

            print " "


        print " "
        
                            

    def printheapmap(self):

        ############################print data.dataremodel####################
        x =  np.zeros((self.longitudebinnum + 1),float)
        y =  np.zeros((self.latitudenum + 1),float)

        for i in range(0,self.longitudebinnum + 1): x[i] = self.longitudemin + i * self.Interval    ####set the x y rais word(number)
        for i in range(0,self.latitudenum + 1): y[i] = self.latitudemin + i * self.Interval

        intensity =  np.zeros((self.latitudenum,self.longitudebinnum),float)

        for i in range(0, self.latitudenum):  ######## set the map 
            for j in range(0,self.longitudebinnum):
                intensity[i][j] = self.dataremodel[self.latitudenum - 1 - i][j] 




        #setup the 2D grid with Numpy
        x, y = np.meshgrid(x, y)

        #convert intensity (list of lists) to a numpy array for plotting
        intensity = np.array(intensity)

        #now just plug the data into pcolormesh, it's that easy!
        plt.pcolormesh(x, y, intensity,cmap=plt.cm.Reds)
        #plt.pcolor(intensity,cmap=plt.cm.Reds)
        plt.colorbar() #need a colorbar to show the intensity scale
        plt.show() #boom




        ############################print data.dataremodel####################

