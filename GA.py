
import earthquakedata

#import randommodel.py

class GA():
    def __init__(self):
        self.a = 1
        self.Population = 500
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

    def main(self):

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

        #here's our data to plot, all normal Python lists

        data.printmap()

    ################# simple Log Likelihood  Evaluate  #########################



    def Evalate(self,testintegerrandomforecat):

        
        Likelihood = 0

        for i in range(0,data.latitudenum):
            for j in range(0,data.longitudebinnum):##
                Likelihood += ( -testintegerrandomforecat[i][j] + data.dataremodel[i][j] * math.log(testintegerrandomforecat[i][j]) - math.log( math.factorial( data.dataremodel[i][j])) )    ####had problem 


        return Likelihood



    ######################################################################




     
    ########################### selection #################################

    def tournament_selection(self,model): #not complete
        fitneesum = 0

        for i in range(0,Population): #more chonces choose better one
            fitneesum += model[i].score
        prob  =  np.zeros(Population,float)
          

    def random_selection(self,model):

        cn = 0
        used_Pop = np.zeros(Population,float)

        while cn < Tournament_size:
            rand = random.uniform(1,Tournament_size)
            if used_Pop[rand] == 0:

                used_Pop[rand] = 1
                pool.add(model[rand])




     

    ######################################################################



    ########################## CROSSOVER ##################################

    def Corssover(self,modelA,modelB):
        for i in range(0, modelA.latitudenum):  ######## set the map 
            for j in range(0,modelA.longitudebinnum):
                if random.uniform(0,1) > Crossover_Chance :
                    temp = modelA.dataremodel[i][j]
                    modelA.dataremodel[i][j] = modelB.dataremodel[i][j]
                    modelB.dataremodel[i][j] = temp


    ######################################################################





    ########################M  Mutation   #################################
    def Mutation(self,model):
        for i in range(0 , Population):
            if random.uniform(0,1) > Mutation_Chance_individual:

                for j in range(0, model[i].latitudenum):  ######## set the map 
                    for k in range(0, model[i].longitudebinnum):
                        if random.uniform(0,1) >  Mutation_Chance_chchromosome:
                            model[i].dataremodel[j][k] = random.uniform(0,1)





    #######################################################################








