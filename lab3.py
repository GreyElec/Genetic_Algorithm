import random
import time


class Step1():
	def barGo(self, prob: str, rep: int):
		probVect = list(map(float, prob.split(' ')))
		res = list()
		for i in range(rep):
			res.append(sum(list(map(lambda x: 1 if random.random() <= x else 0, probVect))))
		# if __name__ == '__main__':
		#	print(res[-1])
		return res


class Step2(Step1):
	def task2(self, clue: str, state: bool, crowded: bool):
		clue_list = list(map(float, clue.split(' ')))
		Num = int(clue_list[0])
		data = clue_list[1:]
		key = [bool(i) * Num ** Num + i for i in range(Num)]
		# prob = [data[each] for each in key]
		new_data = []
		for each in key:
			temp = []
			temp2 = []
			for i in range(1, Num + 1):
				temp.append(data[each + i])
				temp2.append(data[each + Num + i])
			new_data.append([temp, temp2])
		ind = list(map(int, [state, not (crowded)]))
		p = new_data[ind[0]][ind[1]]
		prob = random.random()
		left = 0.0
		right = 0.0
		for i in range(len(p)):
			left = left + float(int(bool(i)) * p[i - 1])
			right = right + p[i]
			if left <= prob <= right:
				s = i
				d = i
				return s, d

	def Run(self, clue: str, state: bool, crowded: bool, rep: int):
		res = [self.task2(clue=clue, state=state, crowded=crowded) for i in range(rep)]
		# for each in res:
		#	print(each)
		return res


# -strategy "2/ 0.1/ (0.0 1.0) (1.0 0.0) 1.0/ (0.9 0.1) (0.9 0.1)"
'''
class Genetic():
	def __init__(self):
		self.mu = 0.2
		self.Generation = 1
		self.population = 200

	def Create(self, state: int):
		ps = [float('{:.1f}'.format(random.random())) for i in range(state)]
		s = float('{:.1f}'.format(sum(ps)))
		ps = list(map(lambda x: float('{:.1f}'.format(x)), [i / s for i in ps]))
		res = []
		res.append(state)
		for i in range(state):
			res.append(ps[i])
			for i in range(state):
				probtemp = [float('{:.1f}'.format(random.random())) for i in range(state)]
				m = sum(probtemp)
				probtemp = list(map(lambda x: float('{:.1f}'.format(x)), [i / m for i in probtemp]))
				res.extend(probtemp)
		return res
'''


class Step3(Step2):
	def __init__(self):
		self.strategyNum = 20

	def StrategyInit(self, state: int):
		ps = [float('{:.1f}'.format(random.random())) for i in range(state)]
		s = float('{:.1f}'.format(sum(ps)))
		if s == 0:
			s = 1
		ps = list(map(lambda x: float('{:.1f}'.format(x)), [i / s for i in ps]))
		res = []
		res.append(state)
		for i in range(state):
			res.append(ps[i])
			for i in range(state):
				probtemp = [float('{:.1f}'.format(random.random())) for i in range(state)]
				m = sum(probtemp)
				if m == 0:
					m = 1
				probtemp = list(map(lambda x: float('{:.1f}'.format(x)), [i / m for i in probtemp]))
				res.extend(probtemp)
		return res

	def strategySet(self, Num: int, state: int):
		strategySet = [self.StrategyInit(state) for i in range(Num)]
		# print(strategySet)
		return strategySet

	def movement_init(self, population: int, StrategySet: list, state: int):
		# StrategySet = self.strategySet(StrategyNum, state)
		# print(StrategySet)
		res = []
		eva_all = []
		crowded_next = []
		for strategy in StrategySet:
			clue_list = strategy
			data = clue_list[1:]
			key = [bool(i) * state ** state + i for i in range(state)]
			prob = [data[each] for each in key]
			pop_state = [0] * population
			for i in range(population):  # initiate the state and calculate the crowded situation,
				cer = random.random()
				temp = sorted(prob)
				for each in temp:
					if cer <= each:
						pop_state[i] = prob.index(each)

			# if cer < prob[0]:
			#	pop_state.append(0)
			# else:
			#	pop_state.append(1)
			crowded = (sum(pop_state) >= 0.6 * population)
			new_data = []
			for each in key:
				temp = []
				temp2 = []
				for i in range(1, state + 1):
					temp.append(data[each + i])
					temp2.append(data[each + state + i])
				new_data.append([temp, temp2])
			next_move = []
			for i in range(len(pop_state)):
				a = int(pop_state[i])
				b = int(not (crowded))
				temp = 1 if random.random() <= new_data[a][b][1] else 0
				next_move.append(temp)
			attendance = next_move.count(1)
			crowded_next.append(int(attendance >= 0.6 * population))
			# print(crowded_next)
			evaluate = next_move.count(1) if crowded_next[-1] == 0 else next_move.count(0)
			# print(len(next_move))
			res.append(next_move)
			eva_all.append(evaluate)
		# print(len(pop_state))
		# print(population)
		return res, eva_all, crowded_next

	def process_in_week(self, strategy: list, current_state: list, crowded: list):
		crowd = [0] * len(crowded)
		eva = [0] * len(strategy)
		for Index in range(len(current_state)):
			state = current_state[Index]
			method = strategy[Index][1:]
			key = [bool(i) * state ** state + i for i in range(state)]
			new_data = []
			for each in key:
				temp = []
				temp2 = []
				for k in range(1, state + 1):
					temp.append(method[each + k])
					temp2.append(method[each + state + k])
				new_data.append([temp, temp2])
			next_move = []
			for j in range(len(state)):
				temp = 1 if random.random() <= new_data[state[j]][int(not (crowded[Index]))][1] else 0
				next_move.append(temp)
			attendance = next_move.count(1)
			crowd[Index] = int(attendance >= 0.6 * population)
			eva[Index] = next_move.count(1) if crowd[-1] == 0 else next_move.count(0)
		return next_move, crowd, eva


'''         
	def process_in_generation(self, weeks: int, state: int, population: int, Strategy: list):
		state_week1, evaluate, crowd = self.movement_init(population=population, StrategySet=Strategy, state=state)
		outPass = []
		Res = state_week1
		# for i in range(len(Res)):
		# print(Res[i])
		#	for j in range(len(Res[i])):
		#		print(Res[i][j])

		crowded = crowd
		eva = evaluate

		for i in range(weeks - 1):
			# for ind in range(len(Strategy)):
			# Res = state_week1
			# temper = state_week1[ind][1]
			# print(len(Res))
			# crowded = crowd
			# eva = evaluate
			# for i in range(weeks - 1):
			# count_temp = int(len(Strategy))
			for ind in range(len(Res)):
				clue_list = Strategy[ind]
				data = clue_list[1:]
				key = [bool(i) * state ** state + i for i in range(state)]
				new_data = []
				for each in key:
					temp = []
					temp2 = []
					for k in range(1, state + 1):
						temp.append(data[each + k])
						temp2.append(data[each + state + k])
					new_data.append([temp, temp2])
				next_move = []
				str_sta = Res[ind]
				print('strategy:', ind, 'is:', str_sta)
				for j in range(len(Res[ind])):
					a = str_sta[j]
					b = int(not (crowded[i]))
					temp = 1 if random.random() <= new_data[a][b][1] else 0
					next_move.append(temp)
				j = 0
				attendance = next_move.count(1)
				crowded_next = int(attendance >= 0.6 * population)
				eva[ind] = eva[ind] + (next_move.count(1) if crowded_next == 0 else next_move.count(0))
				Res = next_move
				crowded = crowded_next
			outPass.append(eva)
		new_out = list(zip(Strategy, outPass))
		return new_out
'''


def mutation(self, input: list, mu: float):
	tar = input
	p = random.random()
	for i in range(len(tar)):
		if p <= mu:
			tar[i] = '{:.1f}'.format(random.random())
	return tar


def crossover(self, x: list, y: list):
	x_new = []
	y_new = []
	for i in range(len(x)):
		if random.random() >= 0.5:
			x_new.append(x[i])
		else:
			x_new.append(y[i])
	for i in range(len(y)):
		if random.random() >= 0.5:
			y_new.append(y[i])
		else:
			y_new.append(x[i])
	return x, y


def Generation(self, Generation: int, state: int, populationsize: int, week: int):
	Strategy = self.strategySet(Num=self.strategyNum, state=state)
	for i in range(Generation):
		eva = sorted(
			self.process_in_generation(weeks=week, state=state, population=populationsize, Strategy=Strategy),
			key=lambda x: x[1])
		method, evaluate_pre = map(list, list(zip(*eva)))
		x = method[0]
		del (method[0])
		y = method[1]
		del (method[0])
		mu = float(1.0 / (2 * Generation))
		x, y = self.crossover(x, y)
		x = self.mutation(input=x, mu=mu)
		y = self.mutation(input=x, mu=mu)
		method.append(x)
		method.append(y)
		Strategy = method
	return Strategy[0]


# stra = "2 0.1 0.0 1.0 1.0 0.0 1.0 0.9 0.1 0.9 0.1"
# state = 0
# crowded = 1
# s2 = Step2()

# x1 = s2.Run(clue=stra, state=state, crowded=crowded, rep=5)
# print(x1)
state = 2
week = 54
gener = 20
pop = 20
s3 = Step3()
# res, eva_all, crowded_next = s3.movement_init(population=20, StrategySet=s3.strategySet(Num=20, state=2), state=2)
# print('*********')
# print(len(res))
# print('       ')
# print(eva_all)
# print('_________')
# print(crowded_next)
strategy,state,crowded = s3.movement_init(population=20,StrategySet=s3.StrategyInit(2),state=2)

