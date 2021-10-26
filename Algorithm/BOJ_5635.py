N = int(input())
info = [input().split() for _ in range(N)]
info.sort(key = lambda x:(int(x[3]),int(x[2]),int(x[1])))
print(info[-1][0])
print(info[0][0])