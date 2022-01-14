import sys
input = sys.stdin.readline

for _ in range(int(input())):
  wear = {}
  answer = 1

  for _ in range(int(input())):
    a,b = input().strip().split()
    try: wear[b] += 1
    except: wear[b] = 1
    
  for w in wear:
    answer *= (wear[w]+1)
  
  print(answer-1)