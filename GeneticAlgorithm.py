import random
import math

class GeneticAlgorithm():
	def mutation(self, X: str, mu: float):
		X = list(X)
		for i in range(0, len(X)):
			temp = random.random()
			if temp < mu:
				X[i] = str(int(math.fabs(int(X[i]) - 1)))
		X = ''.join(X)
		return X
	def crossover(self, X: str, Y: str):
		temp = [0] * len(X)
		for i in range(0, len(X)):
			p = random.random()
			temp[i] = X[i] if p > 0.5 else Y[i]
		temp = ''.join(temp)
		return temp
	def oneMAX(self, X: str):
		evaluate = sum([int(i) for i in X])
		return evaluate
	def tenornament(self, X, k: int, mu: float):
		# print(X)
		if k > len(X):
			return False
		else:
			ans = []
			clue = []
			m = len(X)
			x = []
			for i in range(0, m):
				x.append(self.oneMAX(X[i]))
			Out = list(zip(x, X))
			x = sorted(Out, key=lambda x: x[0], reverse=True)
			while not (len(ans) == k):
				p = random.random()
				a = 0
				b = 0
				for j in range(0, m):
					a = a + bool(j) * mu * (1 - mu) ** (j - 1)
					b = b + mu * (1 - mu) ** (j)
					if a < p <= b:
						ans.append(str(x[j][1]))
						clue.append(j)
						break
					else:
						continue
			x = list(zip(*x))
			return ans[:], x[1], clue[:]
	def Genetic(self, X):
		for i in range(400):
			[X2, X1, ind] = self.tenornament(X, 2, 0.6)
			x_new = self.crossover(X2[0], X2[1])
			x_new2 = self.crossover(X2[0], X2[1])
			x_new = self.mutation(x_new, 0.2)
			x_new2 = self.mutation(x_new2, 0.2)
			X1 = list(X1)
			X1[ind[0]] = x_new
			X1[ind[1]] = x_new2
		m = len(X1)
		x = []
		for i in range(m):
			x.append(self.oneMAX(X1[i]))
		Out = list(zip(x, X1))
		Out = sorted(Out, key=lambda x: x[0],reverse=True)
		return Out
test = ['10101', '11111', '00000', '10000', '11000', '11100', '11110', '10111', '11011', '11101', '10000', '10001',
        '10011', '10111']
app = GeneticAlgorithm()
ans = app.Genetic(test)
#print(ans)
print(ans[0][1])
