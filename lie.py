b = 2
a = [2,5,8,4,6]
temp = [b*2**i for i in range(len(a))]
ans = 0
for each in temp:
	if each in a and each > ans:
		ans = each
print(ans*2)
