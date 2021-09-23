import sys
x = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    code = sys.stdin.readline().strip()
    if x in code:
        cnt+=1
        continue
    for i in range(1,len(x)):
        newcode = code[-i:]+code[:-i]
        if x in newcode:
            cnt += 1
            break
print(cnt)