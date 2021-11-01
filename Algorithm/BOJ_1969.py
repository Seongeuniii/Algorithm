N,M = map(int,input().split())
dna = [input() for _ in range(N)]
result = ''
cnt = 0
for i in range(M):
  dic = {'A':0, 'C':0, 'G':0, 'T':0}
  for j in range(N):
    dic[dna[j][i]] += 1
  li = list(zip(dic.keys(),dic.values()))
  li.sort(key=lambda x: x[1], reverse=True)
  result += li[0][0]
  cnt += (N-li[0][1])
print(result)
print(cnt)