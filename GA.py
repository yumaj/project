import earthquakedata
import randommodel
import numpy as np
import math
import random
import UNDX
import new_UNDX

class GA():
    def __init__(self):
        self.Population_size = 100
        self.Tournament_size = 50
        self.Generation = 200
        self.Crossover_Chance = 0.9
        self.Mutation_Chance_individual = 0.8


        self.longitudemax = 145
        self.longitudemin = 140
        self.latitudemax = 35
        self.latitudemin = 30

        self.Interval = 0.5
        self.Mutation_Chance_chchromosome =  1/( (int)((self.longitudemax - self.longitudemin)/self.Interval) * (int)((self.latitudemax - self.latitudemin)/self.Interval) )
        self.Population = []
        self.newpool = []

        self.longitudebinnum = (int)((self.longitudemax - self.longitudemin)/self.Interval)   #how many bins 
        self.latitudenum = (int)((self.latitudemax - self.latitudemin)/self.Interval)  #how many bins 
        self.Mutation_Chance_chromosome = 1/(self.latitudenum * self.longitudebinnum)
    ################# simple Log Likelihood  Evaluate  #########################


    def Evalate(self,testintegerrandomforecat,data):
        Likelihood = 0
        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):##
                Likelihood += (-testintegerrandomforecat[i][j] + data.dataremodel[i][j] * math.log(testintegerrandomforecat[i][j]) - math.log( math.factorial( int(data.dataremodel[i][j]) )) )    ####had problem 
        return Likelihood
     
    ########################### selection #################################

    def tournament_selection(self):
        for i in range(0, self.Tournament_size):
            self.newpool.append(self.Population[i])

    ######################################################################



    ########################## CROSSOVER ##################################

    def Corssover(self):
        need = 100

        while need != 0:
            changenum = random.randint(0,self.latitudenum * self.longitudebinnum / 3)
            Pa = random.randint(0,len(self.newpool) -1)
            Pb = random.randint(0,len(self.newpool) -1)
            Pc = random.randint(0,len(self.newpool) -1)

            while Pa == Pb or Pa == Pc or Pb == Pc:
                Pa = random.randint(0,len(self.newpool) -1)
                Pb = random.randint(0,len(self.newpool) -1)
                Pc = random.randint(0,len(self.newpool) -1)   
            counter = 0
            Ca = np.zeros((self.latitudenum ,self.longitudebinnum ),float)
            Cb = np.zeros((self.latitudenum,self.longitudebinnum),float)
            rc = random.uniform(0,1)
            if rc < self.Crossover_Chance:
                new_UNDX.UNDX(self.newpool[Pa], self.newpool[Pb], self.newpool[Pc], Ca, Cb ,self.latitudenum, self.longitudebinnum)                  
                self.Population.append(Ca)
                need -= 2
            else :
                self.Population.append(self.newpool[Pa])
                self.Population.append(self.newpool[Pb])
                need -= 2
    def Mutation(self):
        for i in range(0, len(self.Population)):
            irm = random.uniform(0,1)
            if irm > self.Mutation_Chance_individual:
                for k in range(0, self.latitudenum):
                    for j in range(0, self.longitudebinnum):
                        rm = random.uniform(0,1)
                        if rm > self.Mutation_Chance_chchromosome :
                            self.Population[k][j] = random.uniform(0,1)


    ######################################################################

    def newpoolclear(self):
        while len(self.newpool) != 0 :
            self.newpool.pop()
    def printmodel(self,model):
        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):##
                print model[i][j]," ",
            print ""

    def printpool(self):
        for i in range(0,2):
            self.printmodel(self.Population[i])           
       
    def P_sort(self,score):
        for i in range(0, len(self.Population)):
            for j in range(i + 1, len(self.Population)):
                if score[i] < score[j] :
                    for k in range(0, self.latitudenum):
                        for s in range(0, self.longitudebinnum):
                            temp = self.Population[i][k][s]
                            self.Population[i][k][s] = self.Population[j][k][s]
                            self.Population[j][k][s] = temp
                            stemp = score[i]
                            score[i] = score[j]
                            score[j] = stemp




    def main(self):

        ############ generate model from data ##################
        data = earthquakedata.dataremodel()


        path = 'data.dat'

        ######## map setting #######

        data.longitudemax = 145
        data.longitudemin = 140



        data.latitudemax = 35
        data.latitudemin = 30

        data.Interval = 0.5

        data.datareader(path)

        ######## setting end ######

        data.selectyear = 2010
        data.selectmonths = 1
        data.selectmonthe = 12

        data.setnum()

        data.findhappentimes()



        #data.setmodel()

        #here's our data to plot, all normal Python lists


        ############# from data model end ########################

        ####################### GA start  ########################
        #n  =    1 ###set n times

        #best = Evalate(integerrandomforecat)
       
        ############# first Population ############################
        newPopulation = np.zeros((self.Population_size, data.latitudenum , data.longitudebinnum ),float)
        for i in range(0, self.Population_size):
            newPopulation[i] = randommodel.generatemodel(data.latitudenum , data.longitudebinnum );
        for i in range(0, self.Population_size):
            self.Population.append(newPopulation[i])

        ######### loop ########################    
        best = -100000

        for g in range(0,self.Generation):

            
            score = np.zeros(len(self.Population),float)

            for i in range(0, len(self.Population) ):
                intPopulation = randommodel.intergermodel(self.Population[i], data.latitudenum , data.longitudebinnum );
                score[i] = self.Evalate(intPopulation,data)

            for i in range(0,len(score)):
                if score[i] > best :
                    best = score[i]
            
            self.P_sort(score)

            while len(self.Population) > self.Population_size:
                self.Population.pop()


            score = np.zeros(len(self.Population),float)            
            
            for i in range(0, len(self.Population) ):
                intPopulation = randommodel.intergermodel(self.Population[i], data.latitudenum , data.longitudebinnum )
                score[i] = self.Evalate(intPopulation,data)

            self.P_sort(score)
            self.newpoolclear()
            self.tournament_selection()
            self.Corssover()
            self.Mutation()

        print "GA best = " , best

        return best

