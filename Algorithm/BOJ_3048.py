import sys
input = sys.stdin.readline

A, B = map(int,input().split())
ANT = list(input().strip())[::-1] + list(input().strip())
ant = [i for i in range(A+B)]
T = int(input())

while T:
  T -= 1
  move = [0]*(A+B)
  
  for j in range(A+B-1):
    if not move[j] and ant[j] < A and ant[j+1] >= A:
      ant[j], ant[j+1] = ant[j+1], ant[j]
      move[j+1] = 1

for a in ant:
  print(ANT[a], end='')
