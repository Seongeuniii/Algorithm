import sys,math
input = sys.stdin.readline
N = int(input())
room = list(map(int,input().split()))
B,C = map(int,input().split())
result = N
for i in range(N):
  if room[i] > B:
    result += math.ceil((room[i]-B)/C)
print(result)
