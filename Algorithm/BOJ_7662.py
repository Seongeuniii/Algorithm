from sys import stdin
from heapq import heappop,heappush
T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    dic = {}
    max_heap = []
    min_heap = []
    for _ in range(k):
        cmd = stdin.readline().split()
        cmd[1] = int(cmd[1])
        if cmd[0] == 'I':
            heappush(max_heap,-cmd[1])
            heappush(min_heap,cmd[1])
            try:
                dic[cmd[1]]+=1
            except:
                dic[cmd[1]]=1
        elif cmd[1] == 1:
            while max_heap:
                test = -heappop(max_heap)
                if dic[test] != 0:
                    dic[test] -= 1
                    break
        elif cmd[1] == -1:
            while min_heap:
                test = heappop(min_heap)
                if dic[test] != 0:
                    dic[test] -= 1
                    break
    a_result = False
    max_result = 0
    while max_heap:
            test = -heappop(max_heap)
            if dic[test] != 0:
                max_result = test
                a_result = True
                break
    b_result = False
    min_result = 0
    while min_heap and a_result:
            test = heappop(min_heap)
            if dic[test] != 0:
                min_result = test
                b_result = True
                break
    if b_result:
        print(max_result,min_result)
    else:
        print('EMPTY')