from collections import deque
N = int(input())
card = deque([i for i in range(N,0,-1)])
while len(card)>1:
  card.pop()
  card.appendleft(card.pop())
print(card[0])