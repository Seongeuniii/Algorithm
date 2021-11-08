import sys
input = sys.stdin.readline
N = int(input())
result = 0
p = []
m = []
for _ in range(N):
  n = int(input())
  if n == 1:
    result += 1
  elif n <= 0:
    m.append(n)
  else:
    p.append(n)
t = 1
for i in sorted(m):
  if t == 1:
    t = i
  else:
    result += (t*i)
    t = 1
if t != 1:
  result += t
t = -1
for j in sorted(p, reverse=True):
  if t == -1:
    t = j
  else:
    result += (t*j)
    t = -1
if t != -1:
  result += t
print(result)