class question3():
	def oneMAX(self, X: str):
		evaluate = sum([int(i) for i in X])
		return evaluate
app = question3()
print(app.oneMAX('01000'))