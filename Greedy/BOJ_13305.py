import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))
min_price = price[0]
result = 0
for i in range(N-1):
  if price[i] < min_price:
    min_price = price[i]
  result += road[i]*min_price
print(result)