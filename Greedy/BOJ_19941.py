N, K = map(int, input().split())
table = list(input().strip())
answer = 0

for idx, t in enumerate(table):
  if t == 'P':
    for i in range(max(0, idx-K), min(N, idx+K+1)):
      if table[i] == 'H':
        table[i] = ' '
        answer += 1
        break

print(answer)