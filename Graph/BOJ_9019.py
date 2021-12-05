import sys
from collections import deque
input = sys.stdin.readline

def D(node):
  new_n = node*2
  if new_n >= 10000:
    new_n %= 10000
  return new_n

def S(node):
  new_n = node - 1
  if node == 0:
    new_n = 9999
  return new_n

def L(node):
  str_node = str(node)
  if node >= 1000:
    new_n = int(str_node[1:]+str_node[0])
  else:
    new_n = int(str_node + '0')
  return new_n

def R(node):
  str_node = str(node)
  if node < 1000:
    str_node = '0' + str_node
  if node < 100:
    str_node = '0' + str_node
  if node < 10:
    str_node = '0' + str_node
  new_n = int(str_node[-1] + str_node[:len(str_node)-1])
  return new_n

for _ in range(int(input())):
  A,B = map(int,input().split())
  
  q = deque()
  q.append(A)
  visited = [0]*10000
  parent = [0]*10000
  visited[A] = 1

  while q:
    node = q.popleft()

    nD = D(node)
    if not visited[nD]:
      visited[nD] = 'D'
      parent[nD] = node
      q.append(nD)

    nS = S(node)
    if not visited[nS]:
      visited[nS] = 'S'
      parent[nS] = node
      q.append(nS)

    nL = L(node)
    if not visited[nL]:
      visited[nL] = 'L'
      parent[nL] = node
      q.append(nL)

    nR = R(node)
    if not visited[nR]:
      visited[nR] = 'R'
      parent[nR] = node
      q.append(nR)

    if nD == B or nS == B or nL == B or nR == B:
      break
    
  def dfs(start):
    answer = ''
    node = start
    while node != A:
      answer += visited[node]
      node = parent[node]
    return answer[::-1]

  print(dfs(B))