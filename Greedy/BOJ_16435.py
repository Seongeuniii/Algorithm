import sys
N, L = map(int,sys.stdin.readline().split())
fruit = sorted(list(map(int,sys.stdin.readline().split())))
i = 0
while fruit[i]<=L:
    L+=1
    i+=1
    if i==N:
        break
print(L)