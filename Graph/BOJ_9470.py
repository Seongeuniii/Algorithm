import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K, M, P = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    indeg = [0]*(M+1)
    strahler = [[0, 0] for _ in range(M+1)]

    for _ in range(P):
        A, B = map(int, input().split())
        graph[A].append(B)
        indeg[B] += 1

    stack = []

    for i in range(1, M+1):
        if not indeg[i]:
            strahler[i] = [1, 1]
            stack.append(i)

    while stack:
        node = stack.pop()
        for nd in graph[node]:
            indeg[nd] -= 1
            if strahler[nd][0] == strahler[node][0]:
                strahler[nd][1] += 1
            elif strahler[nd][0] < strahler[node][0]:
                strahler[nd][0] = strahler[node][0]
                strahler[nd][1] = 1
 

            if not indeg[nd]:
                stack.append(nd)
                if strahler[nd][1] > 1: strahler[nd][0] += 1

    print(K, strahler[M][0])