from collections import Counter
n = int(input())
m = Counter(list(map(int,input().split())))
k = int(input())
income = 0
for _ in range(k):
    size,value = map(int,input().split())
    if m[size]:
        m[size] = m[size] - 1
        print(m[size])
        income = income + value
        print(income)
        continue
    else:
        continue
print(income)