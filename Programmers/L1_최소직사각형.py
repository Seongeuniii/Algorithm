# 2분

def solution(sizes):
    long = 0
    short = 0
    
    for w, h in sizes:
        long = max(long, max(w,h))
        short = max(short, min(w,h))
        
    return long * short