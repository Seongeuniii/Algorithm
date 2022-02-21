N = int(input())
topList = list(map(int,input().split()))
stack = []
answer = []

for i in range(N):
  while stack:
    if topList[stack[-1]] >= topList[i]:
      break
    else:
      stack.pop()

  if stack:
    answer.append(stack[-1] + 1)
  else:
    answer.append(0)

  stack.append(i)

print(' '.join(map(str,answer)))