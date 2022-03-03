from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    priorities.sort()
    
    while queue:
        i, q = queue.popleft()
        p = priorities.pop()
        
        if p > q:
            queue.append((i, q))
            priorities.append(p)
        else:
            answer += 1
            if i == location:
                return answer