import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
tree = {}
root = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
for i in range(n):
    if root[i] == -1:
        start = i
    else:
        try:
            tree[root[i]].append(i)
        except:
            tree[root[i]] = [i]
cnt = 0
def dfs(root):
    global cnt
    if root in tree:
        for l in tree[root]:
            if l == x and len(tree[root]) == 1:
                cnt += 1
            elif l == x:
                continue
            else:
                dfs(l)
    else:
        cnt += 1
if start == x:
    print(0)
else:
    dfs(start)
    print(cnt)