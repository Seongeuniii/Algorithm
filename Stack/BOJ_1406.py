import sys
left = list(sys.stdin.readline().strip())
right = []
M = int(input())
for _ in range(M):
  cmd = list(sys.stdin.readline().strip().split())
  if cmd[0] == 'P':
    left.append(cmd[1])
  elif cmd[0] == 'L':
    if left:
      right.append(left.pop())
  elif cmd[0] == 'B':
    if left:
      left.pop()
  else:
    if right:
      left.append(right.pop())
print(''.join(left)+''.join(reversed(right)))
