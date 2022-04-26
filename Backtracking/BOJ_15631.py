def printer():
    print(' '.join(map(str, answer)))
    
def recursive(idx, x):
    if idx == M:
        printer()
        return
    
    for i in range(x, N+1):
        answer[idx] = i
        recursive(idx+1, i+1)
        
N, M = map(int, input().split())
answer = [0]*M

recursive(0, 1)