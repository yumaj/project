import earthquakedata
import randommodel
import numpy as np
import math
import random


class GA():
    def __init__(self):
        self.Population_size = 100
        self.Tournament_size = 100
        self.Generation = 100
        self.Crossover_Chance = 0.9
        self.Mutation_Chance_individual = 0.8

        self.longitudemax = 145
        self.longitudemin = 140
        self.latitudemax = 35
        self.latitudemin = 30

        self.Interval = 1
        self.Mutation_Chance_chchromosome =  1/( (int)((self.longitudemax - self.longitudemin)/self.Interval) * (int)((self.latitudemax - self.latitudemin)/self.Interval) )
        self.Population = []
        self.newpool = []
        self.chagenum = 100

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
            self.printmodel(self.Population[i])


    def Evalate(self,testintegerrandomforecat,data):

        
        Likelihood = 0

        for i in range(0,self.latitudenum):
            for j in range(0,self.longitudebinnum):##
                Likelihood += ( -testintegerrandomforecat[i][j] + data.dataremodel[i][j] * math.log(testintegerrandomforecat[i][j]) - math.log( math.factorial( int(data.dataremodel[i][j]) )) )    ####had problem 


        return Likelihood



    ######################################################################

    ######################### change point ###############################
    def suffle(self):
        for i in range(0 , self.chagenum):
            changepointa = random.randint(0,len(self.Population) - 1)
            changepointb = random.randint(0,len(self.Population) - 1)

            self.Population[changepointa] , self.Population[changepointb] =  self.Population[changepointb] , self.Population[changepointa]





    ######################################################################

    def Populationclear(self):
        while len(self.Population) != 0:
            self.Population.pop()

    def newpoolclear(self):
        while len(self.newpool) != 0 :
            self.newpool.pop()
               
       
     
    ########################### selection #################################

    def tournament_selection(self,score): #not complete

        for i in range(0, self.Population_size, 2):
            ip = i + 1
            if score[i] > score[ip]:
                self.newpool.append(self.Population[i]) 
            else :
                self.newpool.append(self.Population[ip])

    def tournament_selection_s(self,score): #not use
        for i in range(0, len(self.Population)):
            for j in range(i + 1, len(self.Population)):
                if score[i] < score[j] :
                    self.Population[i] , self.Population [j] = self.Population[j] , self.Population[i]
                    score[i] , score[j] = score[j] , score[i]

        print score[0],""
        print " "
        for i in range(0, len(self.Population)/2):
            self.newpool.append(self.Population[i])


    ######################################################################

    ########################M  Mutation   #################################
    def Mutation(self,model):
        for j in range(0, self.latitudenum):  ######## set the map 
            for k in range(0, self.longitudebinnum):
                if random.uniform(0,1) <  self.Mutation_Chance_chchromosome:
                    model[j][k] = random.uniform(0,1)



    #######################################################################

    ########################## CROSSOVER ##################################

    def Corssover(self):
        need = self.Tournament_size

        while need != 0:
            changenum = random.randint(0,self.latitudenum * self.longitudebinnum / 3)
            childpointa = random.randint(0,len(self.newpool) -1)
            childpointb = random.randint(0,len(self.newpool) -1)

            while childpointa == childpointb :
                childpointb = random.randint(0,len(self.newpool) - 1)
           
            childa = self.newpool[childpointa]
            childb = self.newpool[childpointb]

            counter = 0
            rc = random.uniform(0,1)
            if rc < self.Crossover_Chance:
                cut = random.randint(0,2)
                cutstart = cut * self.latitudenum * self.longitudebinnum / 3
                cx = cutstart / self.latitudenum
                cy = cutstart % self.longitudebinnum
                while counter < (self.latitudenum * self.longitudebinnum / 3) :
                    changetemp = childa[cx][cy]
                    childa[cx][cy] = childb[cx][cy]
                    childb[cx][cy] = changetemp
                    cy += 1
                    counter += 1
                    if cy >= self.longitudebinnum :
                        cy = 0
                        cx += 1


            rm = random.uniform(0,1)
            if rm < self.Mutation_Chance_individual:
                self.Mutation(childa)
            rm = random.uniform(0,1)
            if rm < self.Mutation_Chance_individual:
                self.Mutation(childb)
            self.Population.append(childa)
            self.Population.append(childb)

            need -= 2


    ######################################################################







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


            intPopulation= np.zeros((len(self.Population), data.latitudenum , data.longitudebinnum ),float)
            score = np.zeros(len(self.Population),float)

            for i in range(0, len(self.Population) ):
                intPopulation[i] = randommodel.intergermodel(self.Population[i], data.latitudenum , data.longitudebinnum );

            for r in range(0, len(self.Population) ):
                score[r] = self.Evalate(intPopulation[r],data)
            

            for i in range(0,len(score)):
                if score[i] > best :
                    best = score[i]


            self.newpoolclear()

            self.suffle()

            self.tournament_selection(score)

            
            self.suffle()

            for i in range(0, len(self.Population) ):
                intPopulation[i] = randommodel.intergermodel(self.Population[i], data.latitudenum , data.longitudebinnum )

            for r in range(0, len(self.Population) ):
                score[r] = self.Evalate(intPopulation[r],data)

            self.tournament_selection(score)

            self.Corssover()

            intPopulation= np.zeros((len(self.Population), data.latitudenum , data.longitudebinnum ),float)
            score = np.zeros(len(self.Population),float)

            for i in range(0,len(self.Population)):
                for j in range(i + 1, len(self.Population)):
                    if score[i] < score[j]:
                        score[i] , score[j] = score[j] , score[i]
                        self.Population[i] , self.Population[j] = self.Population[j] , self.Population[i]

            while len(self.Population) > self.Population_size:
                self.Population.pop()



        print "GAbest = " , best

        return best

