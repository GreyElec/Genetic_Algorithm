import random
import math


class question5():

	def mutation(self, X: str, chi: float, rep: int):
		mu = chi/len(X)
		for i in range(0, rep):
			X = list(X)
			for i in range(0, len(X)):
				temp = random.random()
				if temp < mu:
					X[i] = str(int(math.fabs(int(X[i]) - 1)))
			X = ''.join(X)
		return (X)

	def crossover(self, X: str, Y: str, rep: int):
		for i in range(0, rep):
			temp = [0] * len(X)
			for i in range(0, len(X)):
				p = random.random()
				temp[i] = X[i] if p > 0.5 else Y[i]
			temp = ''.join(temp)
		return temp

	def oneMAX(self, X: str):
		evaluate = sum([int(i) for i in X])
		return evaluate

	def tournament(self, X: list, k: int, rep: int):
		X = X
		mu = 1 / len(X)
		if k > len(X):
			return False
		else:
			for i in range(rep):
				x = []
				ans = [0]*k
				m = len(X)
				for i in range(0, m):
					x.append(self.oneMAX(X[i]))
				Out = list(zip(x, X))
				x = sorted(Out, key=lambda x: x[0], reverse=True)
				i = 0
				while 0 in ans:
					p = random.random()
					a = b = 0
					for j in range(0, len(X)):
						a = a + bool(j) * mu * (1 - mu) ** (j - 1)
						b = b + mu * (1 - mu) ** (j)
						if a < p <= b:
							m = x[j][1]
							ans[i] = (str(x[j][1]))
							i = i + 1
							break
						else:
							continue
			return ans, X

	def create(self,chi, n, pop):
		X = [0] * n
		for i in range(0, n):
			temp = []
			for j in range(0, pop):
				p = random.random()
				temp.append('1' if p > chi/n else '0')
			X[i] = ''.join(temp)
		return X

	def Genetic(self, chi, n, Lambda, k, Rep):
		rep = Rep
		flag = 0
		X = self.create(chi,n, Lambda)
		X1, X = self.tournament(X, k, rep)
		X1[0] = self.crossover(X1[0], X1[1], rep)
		X1[1] = self.crossover(X1[0], X1[1], rep)
		X1[0] = self.mutation(X1[0], chi, rep)
		X1[1] = self.mutation(X1[1], chi, rep)
		X.extend(X1)
		X_eva = []
		for i in range(len(X)):
			X_eva.append(self.oneMAX(X[i]))
		Out = list(zip(X, X_eva))
		Out.sort(key=lambda x: x[0], reverse=True)
		ans = Out[0]
		if ans[1] == n:
			return n, chi, Lambda, k, rep, ans[1], ans[0]
		else:
			while not ans[1] == n and rep<=1000:
				rep = rep + 1
				X1, X = self.tournament(X, k, 1)
				X1[0] = self.crossover(X1[0], X1[1], 1)
				X1[1] = self.crossover(X1[0], X1[1], 1)
				X1[0] = self.mutation(X1[0], chi, 1)
				X1[1] = self.mutation(X1[1], chi, 1)
				X.extend(X1)
				X_eva = []
				for i in range(len(X)):
					X_eva.append(self.oneMAX(X[i]))
				Out = list(zip(X, X_eva))
				Out.sort(key=lambda x: x[0], reverse=True)
				ans = Out[0]
				print(ans[1],rep)
			return n, chi, Lambda, k, rep, ans[1], ans[0]


app = question5()
chi = float(input())
n = int(input())
Lambda = int(input())
k = int(input())
repetitions = int(input())
X = app.create(chi,n, Lambda)
#print(X)
Y = app.mutation(X[1], chi, repetitions)
# print(Y)
Z = app.crossover(X[3], X[4], repetitions)
# print(Z)
Sigma = app.tournament(X, k, repetitions)
#print(Sigma)
print(app.Genetic(chi, n, Lambda, k, repetitions))
