import random

class question2():
	def crossover(self, X: str, Y: str,rep:int):
		for i in range(0,rep):
			temp = [0] * len(X)
			for i in range(0, len(X)):
				p = random.random()
				temp[i] = X[i] if p > 0.5 else Y[i]
			temp = ''.join(temp)
			print(temp)

app = question2()
app.crossover('00000','11111',4)