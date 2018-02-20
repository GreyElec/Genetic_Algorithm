n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
	order = input().split()
	try:
		int(order[1])
	except IndexError:
		eval('s.{}'.format(order[0]))
	else:
		eval('s.{}({})'.format(order[0], order[1]))
print(s)
