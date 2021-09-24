import sys
sys.setrecursionlimit(10 ** 6)
t = int(sys.stdin.readline())
def xfunc(nd):
        stack.append(nd)
        if parent[nd] != 0:
            xfunc(parent[nd])
def yfunc(nd):
    if nd in stack:
        print(nd)
        return
    if parent[nd] != 0:
        yfunc(parent[nd])
for _ in range(t):
    n = int(sys.stdin.readline())
    parent = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        parent[b] = a
    stack = []
    x,y = map(int,sys.stdin.readline().split())
    xfunc(x)
    yfunc(y)