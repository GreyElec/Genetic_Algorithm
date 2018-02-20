from itertools import product

param = input().split()
param2 = [list(param[0])]*int(param[1])
temp = list((product(param2[0],param2[1])))
ans = []
for i in range(len(temp)):
	if temp[i][0] != temp[i][1]:
		ans.append(temp[i])
	else:
		continue
print(sorted(ans,key=lambda x:[x[0],x[1]]))