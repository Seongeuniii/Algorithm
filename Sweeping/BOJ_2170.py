import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort()

answer = 0
s = lines[0][0]
e = lines[0][1]

for i in range(1, N):
  a, b = lines[i]
  if a > e:
    answer += (e-s)
    s = a
    e = b
  else:
    e = max(b, e)

print(answer + (e-s))