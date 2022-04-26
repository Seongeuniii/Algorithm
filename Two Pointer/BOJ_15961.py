import sys
input = sys.stdin.readline

N, d, k ,c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
check = [0]*(d+1)

answer = []
e = 0
type_num = 0
cnt = 0

for s in range(N):
  while cnt < k:
    if not check[sushi[e]]: type_num += 1
    check[sushi[e]] += 1
    cnt += 1
    e += 1
    if e == N: e = 0
  
  if not check[c]: answer.append(type_num+1)
  else: answer.append(type_num)

  if check[sushi[s]] == 1: type_num -= 1
  check[sushi[s]] -= 1
  cnt -= 1

print(max(answer))