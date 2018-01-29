import random


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


app = question4()

app.tournament(['0000', '1111', '1110', '1100', '1000', '0000'], 2, 4)
