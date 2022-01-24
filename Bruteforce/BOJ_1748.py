N = input().strip()
answer = 0
for i in range(1,len(N)):
  answer += 9 * (10**(i-1)) * i
print(answer + ((int(N) - 10**(len(N)-1)) + 1) * len(N))