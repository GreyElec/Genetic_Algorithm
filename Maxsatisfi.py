# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:11:18 2018
@author: privacy
"""
import math
import random
import sys

sys.setrecursionlimit(10000)


class Maxsatis():
	'''
		def __init__(self, question  : int, clause: str, assignment: str):
			self.question = question
			self.clause = list(map(int, clause.split(' ')[1:-1]))
			self.assignment = list(map(int, list(assignment)))
			self.value = list(map(int, list(map(math.fabs, self.clause))))
			self.sign = list(map(int, list(map(lambda x: x / math.fabs(x), self.clause))))
			self.question1(self.assignment,self.sign,self.value)
	'''

	def parameter(self, clause: str):
		# clause = list(map(int,clause.split(' ')))[1:-1]
		value = list(map(int, list(map(math.fabs, clause))))
		sign = list(map(int, list(map(lambda x: x / math.fabs(x), clause))))
		return value, sign

	def question1(self, assignment: str, clause):
		assignment = list(map(int, list(assignment)))
		value, sign = self.parameter(clause)
		if max(value) > len(assignment):  # 简单判断数据是否符合长度要求
			return False
		order = [assignment[each - 1] for each in value]  # 按照要求对数据重新排序
		vari = list(map(int, map(lambda x: str(int(math.fabs(int(x[0]) - 1))) if x[1] < 0 else x[0],
		                         zip(order, sign))))  # 按照数据要求对数据进行 ‘非’ 处理
		if any(vari):
			return True
		else:
			return False


class Excute(Maxsatis):
	def __init__(self, path: str):
		self.f = open(path)
		self.length, self.num, self.data = self.textparse()
		self.para = self.param()

	def textparse(self):
		data = [each.split(' ') for each in self.f]  # 预处理数据，字符串-list

		def func(s: list):
			if s[0] == 'p':
				i, j = s[-2], s[-1]
				return i, j

		i, j = map(int, list(filter(None, map(func, data)))[0])  # 取出数据中的第二行 确定条件数和条件条数
		return i, j, data

	def param(self):
		para = [self.data[-a] for a in range(1, self.num + 1)]  # 取出数据中的条件定义从后向前取
		for i in range(len(para)):
			para[i] = list(filter(None, map(int, para[i])))  # 删除数据开头和结尾的0
		return para

	def excute(self, assignment: str):
		count = 0
		for each in self.para:
			if self.question1(assignment, each):
				count = count + 1
			else:
				continue
		return count


class Genetic(Excute):
	def __init__(self, path):
		super().__init__(path)
		self.mu = 0.2
		self.Generation = 0
		self.population = 20

	def Mute(self, input: str):
		return ''.join(
			list(map(lambda x: str(int(math.fabs(int(x) - 1))) if random.random() < 0.2 else x, list(input))))

	def crossOver(self, x: str, y: str):
		return ''.join(map(lambda a, b: a if random.random() > 0.5 else b, x, y))

	def evaluate(self, assignment: str):
		return self.excute(assignment)

	def popCreate(self):
		return [''.join(['1' if random.random() > 0.5 else '0' for i in range(4)]) for j in range(self.population)]

	def GeneticRun(self, assignment: list):
		# print('Runing')
		ordered = (sorted(zip(assignment, map(self.excute, assignment)), key=lambda x: x[1], reverse=True))
		x, y = ordered[0][0], ordered[1][0]
		x_new = self.crossOver(x, y)
		y_new = self.crossOver(x, y)
		x_new = self.Mute(x_new)
		y_new = self.Mute(y_new)
		ordered, wasted = zip(*ordered)
		ordered = list(ordered)
		ordered[0], ordered[1] = x_new, y_new
		assignment_eval = (sorted(zip(ordered, map(self.excute, ordered)), key=lambda x: x[1], reverse=True))
		try:
			if assignment_eval[0][1] == 4:
				m = self.Generation
				self.Generation = 0
				return m, assignment_eval[0]
			elif self.Generation >= 3000:
				m = self.Generation
				self.Generation = 0
				return m, assignment_eval[0]
			else:
				self.Generation = self.Generation + 1
			return self.GeneticRun(ordered)
		except(RecursionError):
			m = self.Generation
			self.Generation = 0
			return m, assignment_eval[0]


# target = zip(*ordered)
# print(target)


'''
test = Maxsatis()
clause = '0.5 2 1 3 4 0'
clause = clause.split(' ')[1:-1]
clause = list(map(int, clause))
test.question1('1234', clause)
'''

path = r'C:\Users\Silver\Desktop\example.wcnf'
m = Excute(path)
m.excute('0000')

g = Genetic(path)
assignment = g.popCreate()
print(g.GeneticRun(assignment))
