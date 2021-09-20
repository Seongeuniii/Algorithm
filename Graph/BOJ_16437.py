import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
info = [[],['S',0,0]]
graph = [[] for _ in range(n+1)]
for i in range(2,n+1):
    t,a,p = sys.stdin.readline().split()
    a = int(a)
    p = int(p)
    graph[p].append(i)
    info.append([t,a,p])
result = [0 for _ in range(n+1)]
def escape(root,node): #(0,1)
    global result
    for l in graph[node]:
        escape(node,l)
    if info[node][0] == 'S':
        result[root] += (result[node]+info[node][1]) #부모 노드로 양 올려줌
    elif result[node] > info[node][1]: # 한마리라도 살아남은거 올려줌
            result[root] += (result[node]-info[node][1])
escape(0,1)
print(result[1])