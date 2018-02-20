def merge_the_tools(string, k):
	# your code goes here
	sep = int(len(string) / k)
	ans = []
	for i in range(sep, len(string), sep):
		ans.append(string[i - sep:i])
	print('the ans = ',ans)
	for i in range(len(ans)):
		temp = set(list(ans[i]))
		print(temp)

		ans[i] = ''.join(list(temp))
	for each in ans:
		print(each)
merge_the_tools('abbcddeeffgg',4)
