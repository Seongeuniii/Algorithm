import sys, math
input = sys.stdin.readline

def solution():
  answer = math.inf

  for i in range(84):
    cost = 0

    for hill in hills:
      if hill < i:
        cost += (i-hill)**2
      elif hill > i+17:
        cost += (hill-(i+17))**2

    answer = min(answer, cost)    

  return answer

N = int(input())
hills = [int(input()) for _ in range(N)]
print(solution())