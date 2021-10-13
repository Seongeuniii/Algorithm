import sys
S = sys.stdin.readline().strip()
exp = sys.stdin.readline().strip()
stack = []
idx = []
for l in S:
  stack.append(l)
  if exp[0] == l:
    idx.append(0)
    if idx[-1] == len(exp)-1:
        idx.pop()
        stack.pop()
  elif len(idx)!=0:
    if exp[idx[-1]+1] == l:
      idx[-1] += 1
      if idx[-1] == len(exp)-1:
        idx.pop()
        for _ in range(len(exp)):
          stack.pop()
    else:
      idx = []
if len(stack) == 0:
  print('FRULA')
else:
  print(''.join(stack))