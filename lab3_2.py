import random
import time


class Step1():
	def barGo(self, prob: str, rep: int):
		probVect = list(map(float, prob.split(' ')))
		res = list()
		for i in range(rep):
			res.append(sum(list(map(lambda x: 1 if random.random() <= x else 0, probVect))))
		return res


'''
s1 = Step1()
prob = '0.25 0.25 0.25 0.25'
rep = 5
x = s1.barGo(prob=prob, rep=rep)
print(x)
'''


class Step2(Step1):
	def task2(self, clue: str, state: bool, crowded: bool):
		clue_list = list(map(float, clue.split(' ')))
		Num = int(clue_list[0])
		data = clue_list[1:]
		key = [bool(i) * Num ** Num + i for i in range(Num)]
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
		return res


'''
s2 = Step2()
strategy = "2 0.1 0.0 1.0 1.0 0.0 1.0 0.9 0.1 0.9 0.1"
state = 0
crowded = 1
rep = 5
x = s2.Run(clue=strategy, state=state, crowded=crowded, rep=rep)
print(x)
'''


class Step3():
	def __init__(self, population_size=None, states=None, weeks=None, max_t=None):
		self.population_size = population_size
		self.states = states
		self.weeks = weeks
		self.max_t = max_t
		self.mu = 0.2
		self.limit = 0.6 * self.population_size
		self.generation = 0
		self.t0 = time.clock()
		#print(self.t0)
	def strategy_init(self, state: int):
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

	def create_strategy(self, strategy_size: int, state: int):
		return [self.strategy_init(state) for i in range(strategy_size)]

	def parser(self, strategy: list):
		data = strategy[1:]
		state = self.states
		key = [bool(i) * state ** state + i for i in range(state)]
		prob = [data[each] for each in key]
		new_data = []
		for each in key:
			temp = []
			temp2 = []
			for i in range(1, state + 1):
				temp.append(data[each + i])
				temp2.append(data[each + state + i])
			new_data.append([temp2, temp])
		return prob, new_data

	def parsego(self, strategySet: list):
		prob = [0] * len(strategySet)
		data = [0] * len(strategySet)
		for i in range(len(strategySet)):
			prob[i], data[i] = self.parser(strategySet[i])
		return prob, data

	# prob,data = self.parser(strategy=each) for each in strategySet

	def state_init(self, prob: list, population: int):
		temp = sorted(prob)
		state = [0] * population
		for i in range(0, population, 1):
			Num_random = random.random()
			for each in temp:
				if 0 <= Num_random < each:
					state[i] = prob.index(each)
					break
		return state

	def state_init_go(self, probset: list):
		# strategyset = self.create_strategy(strategy_size=self.population_size, state=self.states)
		# probset, _ = self.parsego(strategySet=strategyset)
		return [self.state_init(prob=each, population=self.population_size) for each in probset]

	def crowded_init(self, state_set: list):
		crowded = []
		for each in state_set:
			if each.count(1) > self.limit:
				crowded.append(1)
			else:
				crowded.append(0)
		return crowded

	def weekwork(self, data: list, crowded: list, state: list):
		Num_strategy = len(state)
		state_out = []
		crowded_out = []
		eva = []
		for i in range(Num_strategy):
			new_state = []
			for j in range(self.population_size):
				prob = data[i][crowded[i]][state[i][j]][1]
				prob2 = random.random()
				if 0 <= prob2 < prob:
					new_state.append(1)
				else:
					new_state.append(0)
			temp = 1 if new_state.count(1) >= self.limit else 0
			crowded_out.append(temp)
			state_out.append(new_state)

			eva_temp = new_state.count(1) if temp == 0 else new_state.count(0)
			eva.append(eva_temp)
		'''
		Index = [i for i in range(Num_strategy)]
		over_all = map(list,zip(Index,eva))
		'''

		return state_out, crowded_out, eva

	def generation_work(self, strategyset: list):
		#strategyset = self.create_strategy(self.population_size,self.states)
		probset, Data = self.parsego(strategySet=strategyset)
		state_set = self.state_init_go(probset=probset)
		crowded_set = self.crowded_init(state_set=state_set)
		eva = [0] * len(strategyset)
		for i in range(self.weeks):
			state_temp, crowded_temp, eva_temp = self.weekwork(data=Data, crowded=crowded_set, state=state_set)
			for j in range(len(state_temp)):
				print(i,self.generation,state_temp[j].count(1),crowded_temp[j],*state_temp[j])
			eva = list(map(lambda x, y: x + y, eva, eva_temp))
			state_set = state_temp
			crowded_set = crowded_temp
		strategy_best_one,  eva_store, strategy = self.evaluate(strategyset, eva)
		# eva_overall = list(zip(strategyset,eva))
		# eva_cal = sorted(eva_overall,key=lambda x:x[1],reverse=True)
		# strategy,eva_store = map(list,zip(*eva_cal))
		# strategy_best_one = strategy.pop()
		# eva_store.pop()
		# strategy_best_two = strategy.pop()
		# eva_store.pop()
		return strategy_best_one, strategy, eva_store

	## 接下来要完成 突变和遗传两项任务，然后将新生成的两个策略进行评估并且进行重新排序
	def evaluate(self, strategyset: list, eva: list):  # this function is used to sort the strategy list
		eva_overall = list(zip(strategyset, eva))
		eva_cal = sorted(eva_overall, key=lambda x: x[1], reverse=True)
		strategy, eva_store = map(list, zip(*eva_cal))
		strategy_best_one = strategy.pop()
		eva_store.pop()
		#strategy_best_two = strategy.pop()
		#eva_store.pop()
		return strategy_best_one, eva_store, strategy

	def Mutation(self, In: list):
		data = In[1:]
		out = []
		state = self.states
		key = [bool(i) * state ** state + i for i in range(state)]
		if random.random() < self.mu:
			prob = [data[each] for each in key]
		else:
			prob = self.creat_pair()
		## probability mutation
		for each in key:
			out.append(prob[key.index(each)])
			if random.random() < self.mu:
				temp = data[each+1:each + state+1]
			else:
				temp = self.creat_pair()
			if random.random() < self.mu:
				temp2 = data[each + state + 1:each + state + 1 + state]
			else:
				temp2 = self.creat_pair()
			out.extend(temp)
			out.extend(temp2)
		out.insert(0,self.states)
		return out

		'''		
		for i in range(len(In)):
			if random.random() < self.mu:
				In[i] = float('{:.1f}'.format(random.random()))
		return In
		'''
	def creat_pair(self):
		state = self.states
		probtemp = [float('{:.1f}'.format(random.random())) for i in range(state)]
		m = sum(probtemp)
		if m == 0:
			m = 1
		probtemp = list(map(lambda x: float('{:.1f}'.format(x)), [i / m for i in probtemp]))
		return probtemp

	def crossover(self, In_x: list, In_y: list):
		x = []
		y = []
		state = self.states
		key = [bool(i) * state ** state + i for i in range(state)]
		if random.random() < 0.5:
			data = In_x[1:]
		else:
			data = In_y[1:]
		prob = [data[each] for each in key]
		## probability mutation
		for each in key:
			x.append(prob[key.index(each)])
			if random.random() < 0.5:
				data = In_x[1:]
			else:
				data = In_y[1:]
			temp = data[each + 1:each + state + 1]
			if random.random() < 0.5:
				data = In_x[1:]
			else:
				data = In_y[1:]
			temp2 = data[each + state + 1:each + state + 1 + state]
			x.extend(temp)
			x.extend(temp2)
		x.insert(0,self.states)
		if random.random() < 0.5:
			data = In_y[1:]
		else:
			data = In_x[1:]
		prob = [data[each] for each in key]
		## probability mutation
		for each in key:
			y.append(prob[key.index(each)])
			if random.random() < 0.5:
				data = In_y[1:]
			else:
				data = In_x[1:]
			temp = data[each + 1:each + state + 1]
			if random.random() < 0.5:
				data = In_y[1:]
			else:
				data = In_x[1:]
			temp2 = data[each + state + 1:each + state + 1 + state]
			y.extend(temp)
			y.extend(temp2)
		y.insert(0,self.states)
		#print(x,y)
		return x,y
		'''
		x_new = [In_x[i] if random.random() >= 0.5 else In_y[i] for i in range(len(In_x))]
		y_new = [In_y[i] if random.random() >= 0.5 else In_x[i] for i in range(len(In_x))]
		return x_new, y_new
		'''
	def evacalculate(self, state: list, crowded: list, data: list):
		eva = [0] * len(state)
		state_set = state
		crowded_set = crowded
		for i in range(self.weeks):
			state_temp, crowded_temp, eva_temp = self.weekwork(data=data, crowded=crowded_set, state=state_set)
			eva = list(map(lambda x, y: x + y, eva, eva_temp))
			state_set = state_temp
			crowded_set = crowded_temp
			for j in range(len(state_temp)):
				print(i,self.generation,state_temp[j].count(1),crowded_temp[j],*state_temp[j])
		return eva

	def new_algorithm(self,population_size:int,states:int):
		t1 = time.clock()
		strategyset = self.create_strategy(population_size,states)
		stratege_one ,strategyset,eva_store = self.generation_work(strategyset=strategyset)
		Conditon = True
		while Conditon:
			stratege_one_1 = self.Mutation(In=stratege_one)
			prob,data = self.parser(stratege_one_1)
			new_state = self.state_init()



	def searchalgorithm(self, population_size: int, states: int):
		t1 = time.clock()
		#print(t1)
		strategyset = self.create_strategy(population_size, states)
		strategy_one, strategy_two, strategyset, eva_store = self.generation_work(strategyset)
		# loop starts here
		Condition = True
		while Condition:
			strategy_one_1, strategy_two_1 = self.crossover(In_x=strategy_one, In_y=strategy_two)
			strategy_one_1 = self.Mutation(In=strategy_one_1)
			strategy_two_1 = self.Mutation(In=strategy_two_1)
			search_set = []
			search_set.append(strategy_one_1)
			search_set.append(strategy_two_1)
			prob_search, Data_search = self.parsego(strategySet=search_set)
			state_search = self.state_init_go(probset=prob_search)
			crowded_search = self.crowded_init(state_set=state_search)
		# strategy_search_one, strategy_search_two, eva_search = self.generation_work(search_set)
			eva_temp = self.evacalculate(state=state_search, crowded=crowded_search, data=Data_search)
			strategyset.extend(search_set)
			eva_store.extend(eva_temp)
			strategy_one, strategy_two, eva_store, strategyset = self.evaluate(strategyset=strategyset, eva=eva_store)
			self.generation = self.generation + 1
			t2 = time.clock()
			Condition =  t2-t1 < self.max_t
		#print(t2)
		return strategy_one


population = 10
h = 3
weeks = 10
max_t = 100
s3 = Step3(population_size=population, states=h, weeks=weeks, max_t=max_t)

x = s3.strategy_init(2)
y = s3.strategy_init(2)
#print(len(x))
#print(len(y))
# print(x)
prob, data = s3.parser(x)
# print(prob)
# print(data)
strategy = s3.create_strategy(20, 2)
# print(x)
state = s3.state_init(prob, 20)
# print(state)
x = s3.Mutation(In=x)
y = s3.Mutation(In=y)
#print('*******')
#print(len(x))
#print('*****')
#print(len(y))
#print('******')
#x,y = s3.crossover(x,y)
#print(len(x))
#print('*****')
#print(len(y))
#new = []
#new.append(x)
#new.append(y)
#probSet, Data = s3.parsego(new)

# print(len(probSet))
# print("*******")
# print(len(Data))
#state_set = s3.state_init_go(probSet)
# print(state_set)
# print('length =', len(state_set))
#crowded_init_set = s3.crowded_init(state_set=state_set)
# print(crowded_init_set)
# print('length = ',len(crowded_init_set))
#new_state, new_crowded, eva = s3.weekwork(Data, crowded_init_set, state_set)
# print('new_state:', new_state)
# print('new_crowded:', new_crowded)
#new_strategy = s3.Mutation(strategy)
# print(new_strategy)
# print(len(new_strategy))
#x_new, y_new = s3.crossover(In_x=s3.strategy_init(state=2), In_y=s3.strategy_init(state=2))
#print(x_new)
#print('********')
#print(y_new)

strategy = s3.create_strategy(20, 2)
best_strategy1, best_strategy2, strategy_set, eva_set = s3.generation_work(strategyset=strategy)
#print('best_strategy', best_strategy1, '\n', 'second_strategy:', best_strategy2, '\n', strategy_set, '\n', eva)
strategy = s3.create_strategy(20, 2)
strategy1 = strategy[:2]
probSet,Data = s3.parsego(strategy1)
state = s3.state_init_go(probset=probSet)
crowded = s3.crowded_init(state_set=state)

evacal = s3.evacalculate(state=state,crowded=crowded,data=Data)
#print(evacal)
best = s3.searchalgorithm(population_size=5,states=2)
#print(best)
#print(s3.Mutation(In=x))
