import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(gi):
  global answer

  if gi == 0:
    print(answer)
    sys.exit()

  if not docking[gi]:
    docking[gi] = 1
    answer += 1
    return parent[gi]
  else:
    parent[gi] = dfs(parent[gi])
    return parent[gi]

G = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]
answer = 0
docking = [0]*(G+1)
parent = [-1] + [i for i in range(G)]

for gi in g:
  dfs(gi)

print(answer)