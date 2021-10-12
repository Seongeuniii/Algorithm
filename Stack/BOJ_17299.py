import sys
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().strip().split()))
dic = {}
for l in li:
    try:
        dic[l]+=1
    except:
        dic[l]=1
stack = []
result = []
for i in li[::-1]:
    while len(stack)!=0:
        if dic[stack[-1]] > dic[i]:
            result.append(stack[-1])
            stack.append(i)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        result.append(-1)
        stack.append(i)
for j in result[::-1]:
    print(j, end=' ')