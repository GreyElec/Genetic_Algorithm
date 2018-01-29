import random
import math

class question1():
	def mutation(self,X:str,chi:float,rep:int):
		mu = chi/len(X)
		for i in range(0,rep):
			X = list(X)
			for i in range(0, len(X)):
				temp = random.random()
				if temp < mu:
					X[i] = str(int(math.fabs(int(X[i]) - 1)))
			X = ''.join(X)
			print(X)
app = question1()
app.mutation("00000",2.5,4)