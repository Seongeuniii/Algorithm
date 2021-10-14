T = int(input())
for _ in range(T):
  N = int(input())
  pig = list(map(int,input().split()))
  day = 1
  while sum(pig) <= N:
    newpig = [0 for _ in range(6)]
    newpig[0] = pig[0]+pig[5]+pig[1]+pig[3]
    newpig[1] = pig[1]+pig[0]+pig[2]+pig[4]
    newpig[2] = pig[2]+pig[1]+pig[3]+pig[5]
    newpig[3] = pig[3]+pig[2]+pig[4]+pig[0]
    newpig[4] = pig[4]+pig[3]+pig[5]+pig[1]
    newpig[5] = pig[5]+pig[4]+pig[0]+pig[2]
    pig = newpig
    day+=1
  print(day)