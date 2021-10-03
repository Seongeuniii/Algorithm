import sys
N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort(reverse=True)
result = 0
for i in range(N):
    a = li[i]-i
    if a>0:
        result += a
print(result)