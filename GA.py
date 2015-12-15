import earthquakedata
import randommodel
import numpy as np
import math
import random


class GA():
    def __init__(self):
        self.a = 1
        self.Population_size = 500
        self.Tournament_size = 50
        self.Generation = 100
        self.Crossover_Chance = 0.9
        self.Mutation_Chance_individual = 0.8

        self.longitudemax = 145
        self.longitudemin = 140
        self.latitudemax = 35
        self.latitudemin = 30

        self.Interval = 1
        self.Mutation_Chance_chchromosome =  ( (int)((self.longitudemax - self.longitudemin)/self.Interval) * (int)((self.latitudemax - self.latitudemin)/self.Interval) ) / 1
        self.pool = []
        self.pools = []

        self.longitudebinnum = (int)((self.longitudemax - self.longitudemin)/self.Interval)   #how many bins 
        self.latitudenum = (int)((self.latitudemax - self.latitudemin)/self.Interval)  #how many bins 

    ################# simple Log Likelihood  Evaluate  #########################

    def printmodel(self,model):
        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):##
                print model[i][j]," ",
            print ""

    def printpool(self):
        for i in range(0,2):
            self.printmodel(self.pool[i])


    def Evalate(self,testintegerrandomforecat,data):

        
        Likelihood = 0

        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):##
                Likelihood += ( -testintegerrandomforecat[i][j] + data.dataremodel[i][j] * math.log(testintegerrandomforecat[i][j]) - math.log( math.factorial( int(data.dataremodel[i][j]) )) )    ####had problem 


        return Likelihood



    ######################################################################




     
    ########################### selection #################################

    def tournament_selection(self,model,score): #not complete
        for i in range(0,self.Tournament_size):
            self.pool.append(model[i])
            self.pools.append( score[i])
            self.maintain();

    def maintain(self):
        if len(self.pool) > self.Tournament_size:
            ##sort
            for i in range(0, len(self.pool)):
                for j in range( i + 1, len(self.pool)):
                    if self.pools[i] < self.pools[j]:
                        self.pools[i], self.pools[j] = self.pools[j] , self.pools[i]
                        for pi in range(0,self.latitudenum):
                            for pj in range(0,self.longitudebinnum):
                                ptemp = self.pool[i][pi][pj]
                                self.pool[i][pi][pj] =  self.pool[j][pi][pj]
                                self.pool[j][pi][pj] = ptemp
        while len(self.pool) > self.Tournament_size :
            self.pools.pop()
            self.pool.pop()       


    ######################################################################



    ########################## CROSSOVER ##################################

    def Corssover(self):
        seta = random.randint(0,len(self.pool))
        setb = random.randint(0,len(self.pool))
        if seta != setb:
            for i in range(0, self.latitudenum):  ######## set the map 
                for j in range(0,self.longitudebinnum):
                    if random.uniform(0,1) > self.Crossover_Chance :
                        temp = self.pool[seta][i][j]
                        self.pool[seta][i][j] = self.pool[seta][i][j]
                        self.pool[seta][i][j] = temp


    ######################################################################





    ########################M  Mutation   #################################
    def Mutation(self):
        seta = random.randint(0,self.Tournament_size)
        for i in range(0 , self.Population_size):
            if random.uniform(0,1) > self.Mutation_Chance_individual:

                for j in range(0, self.latitudenum):  ######## set the map 
                    for k in range(0, self.longitudebinnum):
                        if random.uniform(0,1) >  self.Mutation_Chance_chchromosome:
                            self.pool[seta][j][k] = random.uniform(0,1)





    #######################################################################

    def main(self):

        ############ generate model from data ##################
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

        #here's our data to plot, all normal Python lists

        data.printmap()

        ############# from data model end ########################

        ####################### GA start  ########################
        #n  =    1 ###set n times

        #best = Evalate(integerrandomforecat)
        ############# first Population ############################
        for g in range(0,self.Generation):
            Population = np.zeros((self.Population_size, data.latitudenum , data.longitudebinnum ),float)
            score = np.zeros(self.Population_size,float)
            for i in range(0, self.Population_size):
                Population[i] = randommodel.generatemodel(data.latitudenum , data.longitudebinnum );

            ######## Evalate first Population ######

            for r in range(0, self.Population_size):
                score[r] = self.Evalate(Population[r],data)
            
            ######## sort ################
            for i in range(0, self.Population_size):
                for j in range( i + 1, self.Population_size):
                    if score[i] < score[j]:
                        score[i], score[j] = score[j] , score[i]
                        for pi in range(0,self.latitudenum):
                            for pj in range(0,self.longitudebinnum):
                                ptemp = Population[i][pi][pj]
                                Population[i][pi][pj] =  Population[j][pi][pj]
                                Population[j][pi][pj] = ptemp
           




            self.tournament_selection(Population,score)
            self.Corssover()
            self.Mutation()

            print "after:"
            for k in range(0,5):            
                        print self.pools[k]," ",
            print " "

