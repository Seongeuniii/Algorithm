N = int(input())
card = sorted(list(map(int,input().split())))

M = int(input())
find = list(map(int,input().split()))

def binary_search(num):
    s = 0
    e = N-1
    while s <= e :
        mid = (s+e)//2
        if card[mid] == num :
            return 1
        elif card[mid] > num :
            e = mid - 1
        else:
            s = mid + 1
    return 0

for num in find:
    print(binary_search(num), end = ' ')