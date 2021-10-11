import sys
cmd = sys.stdin.readline().strip()
last = 0
stack = []
result = 0
for t in cmd:
    if t=='(':
        stack.append(t)
        last=t
    else: #)
        if t == last:
            stack.pop()
            result+=1
        else:
            stack.pop()
            result+=len(stack)
            last=t
print(result)