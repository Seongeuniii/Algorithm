import sys
n = int(sys.stdin.readline())
stack = []
num = []
result = []
count = 1
for _ in range(n):
    num.append(int(sys.stdin.readline()))
for k in range(n):
    if len(stack) == 0 and count > num[k]:
        print('NO')
        sys.exit()
    if len(stack) != 0 and stack[-1] >= num[k]:
            while len(stack) != 0 and stack[-1] >= num[k]:
                stack.pop()
                result.append('-')
    else:
        for i in range(count, num[k]+1):
            stack.append(i)
            result.append('+')
        count = num[k]+1
        stack.pop()
        result.append('-')
for j in range(len(result)):
    print(result[j])