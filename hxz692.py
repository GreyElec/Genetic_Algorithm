import random
import math


class question1():
	def mutation(self, X: str, chi: float, rep: int):
		mu = chi / len(X)
		for i in range(0, rep):
			X = list(X)
			for i in range(0, len(X)):
				temp = random.random()
				if temp < mu:
					X[i] = str(int(math.fabs(int(X[i]) - 1)))
			X = ''.join(X)
			print(X)


class question2():
	def crossover(self, X: str, Y: str, rep: int):
		for i in range(0, rep):
			temp = [0] * len(X)
			for i in range(0, len(X)):
				p = random.random()
				temp[i] = X[i] if p > 0.5 else Y[i]
			temp = ''.join(temp)
			print(temp)


class question3():
	def oneMAX(self, X: str):
		evaluate = sum([int(i) for i in X])
		return evaluate


class question4():
	def oneMAX(self, X: str):
		evaluate = sum([int(i) for i in X])
		return evaluate

	def tournament(self, X, k: int, rep: int):
		mu = 1 / len(X)
		if k > len(X):
			return False
		else:
			for i in range(0, rep):
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
				print(ans[0])


class question5():

	def mutation(self, X: str, chi: float, rep: int):
		mu = chi / len(X)
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
				ans = [0] * k
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

	def create(self, n, pop):
		X = [0] * pop
		for i in range(0, pop):
			temp = []
			for j in range(0, n):
				p = random.random()
				temp.append('1' if p > 0.5 else '0')
			X[i] = ''.join(temp)
		return X

	def Genetic(self, chi, n, Lambda, k, Rep):
		rep = Rep
		flag = 0
		X = self.create(n,Lambda)
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
			while not int(ans[1]) == n:
				if rep <= 20000:
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
					Out.sort(key=lambda x: x[1], reverse=True)
				# print(Out)
					ans = Out[0]
					print(ans[0],ans[1],rep)
				else:
					break
					return 'cirlce limits'
			# print(ans)
			return n, chi, Lambda, k, rep, ans[1], ans[0]



question = int(input())
print(question)
if question == 1:
	bits_x = str(input())
	chi = float(input())
	repetitions = int(input())
	app = question1()
	app.mutation(bits_x, chi, repetitions)

elif question == 2:
	bits_x = str(input())
	bits_y = str(input())
	repetitions = int(input())
	app = question2()
	app.crossover(bits_x, bits_y, repetitions)

elif question == 3:
	bits_x = str(input())
	app = question3()
	print(app.oneMAX(bits_x))

elif question == 4:
	population = input()
	k = int(input())
	repetitions = int(input())
	app = question4()
	app.tournament(population.split(' '), k, repetitions)

elif question == 5:
	app = question5()
	chi = 0.2
	n = 10
	Lambda = 20
	k = 2
	repetitions = 1
	X = app.create(n, Lambda)
	print(X)
	# print(X)
	Y = app.mutation(X[1], chi, repetitions)
	# print(Y)
	Z = app.crossover(X[3], X[4], repetitions)
	# print(Z)
	Sigma = app.tournament(X, k, repetitions)
	# print(Sigma)
	#print(app.Genetic())
	print(app.Genetic(chi, n, Lambda, k, repetitions))
