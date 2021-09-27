import sys
stack = []
n = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    while len(stack) != 0:
        if stack[-1][1] > top[i]:
            print(stack[-1][0],end=' ')
            stack.append([i+1,top[i]])
            break
        else:
            stack.pop()
    if len(stack) == 0:
        print(0,end=' ')
        stack.append([i+1,top[i]])