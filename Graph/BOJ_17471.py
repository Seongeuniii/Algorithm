import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(group):
  check = [0]*(N+1)

  cnt = population[group[0]]
  check[group[0]] = 1
  q = deque([group[0]])

  while q:
    node = q.popleft()
    for nd in graph[node]:
      if nd in group and not check[nd]:
        cnt += population[nd]
        check[nd] = 1
        q.append(nd)

  return cnt

def solution(N, population):
  people = sum(population)
  answer = people
  area  = [x for x in range(1, N+1)]

  for i in range(1, int(N/2)+1):
    cases = list(combinations(area , i))

    for groupA in cases:
      groupB = list(set(area) - set(groupA))

      sumA = bfs(groupA)
      sumB = bfs(groupB)

      if sumA + sumB == people:
        answer = min(answer, abs(sumA-sumB))
  
  if answer == people:
    return -1
  else:
    return answer

N = int(input())
population = [0] + list(map(int,input().split()))
graph = [[]]

for n in range(1, N+1):
  a, *b = list(map(int,input().split()))
  graph.append(b)

print(solution(N, population))