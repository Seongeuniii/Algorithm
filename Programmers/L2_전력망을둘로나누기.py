def solution(n, wires):
    def dfs(node):
        cnt = 1
        for nd in graph[node]:
            if not check[nd]:
                check[nd] = 1
                cnt += dfs(nd)
        
        dp[node] = cnt
        return dp[node]
                
    dp = [0]*(n+1)
    check = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    check[1] = 1
    dfs(1)
    
    answer = 100
    for i in range(2, n+1):
        diff = abs((n-dp[i]) - dp[i])
        if diff < answer: answer = diff
    
    return answer