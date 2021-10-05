import sys
while True:
    try:
        n ,k = map(int,sys.stdin.readline().split())
        result = n
        while n//k: # 또 먹을 수 있어
            result += n//k
            n = n//k +n%k
        print(result)
    except:
        break