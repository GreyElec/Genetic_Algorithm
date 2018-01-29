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
			# print(len(x) == len(X))
			Out = list(zip(x, X))
			# print('out')
			# print(Out)
			# print('***')
			# print('X')
			# print(X)
			x = sorted(Out, key=lambda x: x[0], reverse=True)
			# print('***')
			# print(x)
			# print('***')
			# print(k)
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
			#print('the x_new is {}'.format(x_new))
			x_new2 = self.crossover(X2[0], X2[1])
			#print('the x_new2 is {}'.format(x_new2))
			x_new = self.mutation(x_new, 0.2)
			#print('the x_new_mut is {}'.format(x_new))
			x_new2 = self.mutation(x_new2, 0.2)
			#print('the x_new2_mut is {}'.format(x_new2))
			X1 = list(X1)
			#print('the origin is {}'.format(X1[ind[0]]))
			X1[ind[0]] = x_new
			#print('the new is {}'.format([ind[0]]))
			#print('the origin2 is {}.'.format(X1[ind[1]]))
			X1[ind[1]] = x_new2
			#print('the new2 is {}'.format(X1[ind[1]]))
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
# print('mutation')
# print(app.mutation('01100', 0.8))
# app.x =
# print(app.x)
# print(app.mutation(app.x, 0.7))
# print('crossover')
# print(app.crossover('00000', '11111'))
# print('oneMAX')
# print(app.oneMAX('110100000000'))

# print("***")
# print(test)
# print('***')
#print(app.tenornament(test, 2, 0.6))
