import sys
N,M = map(int,sys.stdin.readline().split())
value = []
for _ in range(M):
    value.append(int(sys.stdin.readline()))
value.sort(reverse=True)
result = 0
price = 0
for i in range(N):
    if i>=M:
        break
    if value[i]*(i+1)>=result:
        result = value[i]*(i+1)
        price = value[i]
print(price, result)