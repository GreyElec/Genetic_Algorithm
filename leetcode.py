class topmatrix():
	def istopmatrix(self,matrix):
		for i in range(len(matrix) - 1):
			if len(matrix[i + 1]) == i + 2:
				if matrix[i][i] == matrix[i + 1][i + 1]:
					continue
				else:
					return False
			else:
				return False
		return True
app = topmatrix()
print(app.istopmatrix([[18],[66]]))

