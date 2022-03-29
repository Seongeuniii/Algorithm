S = list(input().strip())
answer = 0
cnt = 0
stack = []

while S:
  s = S.pop()

  if s == ')':
    stack.append(cnt)
    stack.append(')')
    cnt = 0

  elif s == '(':
    while stack[-1] != ')':
      cnt += stack.pop()
    stack.pop()
    stack.append(cnt*int(S.pop()))
    cnt = 0

  else:
    cnt += 1

print(sum(stack) + cnt)