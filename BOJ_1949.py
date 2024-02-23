import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
members = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

stack = []

def find_leaf():
    result = []
    
    checked = [0] * (N + 1)
    checked[1] = 1
    q = deque([1])

    while q:
        node = q.popleft()
        stack.append(node)
        cnt = 0

        for nd in tree[node]:
            if checked[nd]: continue

            cnt += 1
            checked[nd] = 1
            q.append(nd)
        
        if (cnt == 0):
            result.append(node)

    return result

dp = [[0, 0, 0] for _ in range(N + 1)]
leaf = find_leaf()

for node in leaf:
    dp[node] = (members[node], 0, 0)

is_child = [0] * (N + 1)
while stack:
    node = stack.pop()
    is_child[node] = 1

    OX = members[node] # 자식 노드 (XO, XX)
    X = 0 # 자식 노드 (O, XO)
    XX = 0 # 자식 노드 XO

    for nd in tree[node]:
        if not is_child[nd]:# 부모 노드 
            continue 
        OX += max(dp[nd][1], dp[nd][2])
        X += max(dp[nd][0], dp[nd][1])
        XX += dp[nd][1]

    dp[node] = [OX, X, XX]

print(max(dp[1]))
