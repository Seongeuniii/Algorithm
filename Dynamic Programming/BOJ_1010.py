import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    up = list(map(int,sys.stdin.readline().split()))
    down = list(map(int,sys.stdin.readline().split()))
    if n == 1:
        print(max(up[0],down[0]))
    else:
        updp = [up[0],down[0]+up[1]]
        downdp = [down[0],up[0]+down[1]]
        for i in range(2,n):
            updp.append(up[i] + max(downdp[i-1],downdp[i-2]))
            downdp.append(down[i] + max(updp[i-1],updp[i-2]))
        print(max(updp[n-1],downdp[n-1]))