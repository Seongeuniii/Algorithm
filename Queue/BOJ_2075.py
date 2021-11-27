import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
  line = list(map(int,input().split()))
  li.extend(line)
  li.sort(reverse=True)
  li = li[:N]
print(li[-1])