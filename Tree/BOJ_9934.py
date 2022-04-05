import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
  global idx

  if node*2 < totalNode and not treeNode[node*2]:
    dfs(node*2)

  treeNode[node] = nums[idx]
  idx += 1

  if node*2+1 < totalNode and not treeNode[node*2+1]:
    dfs(node*2+1)

    
K = int(input())
totalNode = 2**K
nums = list(map(int, input().split()))
treeNode = [0]*totalNode
idx = 0

dfs(1)

for k in range(K):
  for i in range(2**k, 2**(k+1)):
    print(treeNode[i], end=' ')
  print()