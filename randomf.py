import GA
import randommodel
import earthquakedata
import numpy as np

class randomf():
	def __init__(self):
		self.longitudemax = 145
		self.longitudemin = 140
		self.latitudemax = 35
		self.latitudemin = 30
		self.Interval = 1

		self.longitudebinnum = (int)((self.longitudemax - self.longitudemin)/self.Interval)   #how many bins 
		self.latitudenum = (int)((self.latitudemax - self.latitudemin)/self.Interval)  #how many bins 	

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

		best = -100000
		GAf = GA.GA()
		for i in range(0, 200 * 100):
			rf = randommodel.generatemodel(self.latitudenum,self.longitudebinnum)
			intPopulation = np.zeros((data.latitudenum , data.longitudebinnum ),float)
			intPopulation = randommodel.intergermodel(rf,self.latitudenum,self.longitudebinnum)
			score = GAf.Evalate(rf,data)
			if score > best :
				best = score


		print "R best = ", best

		return best

