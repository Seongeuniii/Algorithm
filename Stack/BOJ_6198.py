import sys
input = sys.stdin.readline

N = int(input())
building = list(int(input()) for _ in range(N))
stack = []
answer = 0

for i in range(N-1, -1, -1):
  height = building[i]
  cnt = 0

  while stack and stack[-1][0] < height:
    h, c = stack.pop()
    cnt += (c+1)
  
  stack.append((height, cnt))
  answer += cnt

print(answer)

import sys
input = sys.stdin.readline

stack = []
answer = 0

for _ in range(int(input())):
  h = int(input())

  while stack and h >= stack[-1]:
    stack.pop()
  
  answer += len(stack)
  stack.append(h)

print(answer)