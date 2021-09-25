import sys
n,m = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
know = [] #진실을 아는사람
test = [] #조사해야하는 파티번호
total_party = [0] # 모든 파티

for i in range(1,num[0]+1):
    know.append(num[i])
visited = [0 for _ in range(m+1)]
for g in range(1,m+1):
    party = list(map(int,sys.stdin.readline().split()))
    total_party.append(party[1:])
    for j in know:
        if j in party[1:]:
            test.append(g)
            visited[g] = 1
            break
while test: # 파티 추적
    p = test.pop()
    know = total_party[p]
    for a in know:
        for b in range(1,m+1):
            if visited[b] == 0 and a in total_party[b]:
                test.append(b)
                visited[b] = 1
print(visited.count(0)-1)