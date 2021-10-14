import sys
while True:
  try:
    case = True
    test = list(map(int,input().split()))
    num = [0 for _ in range(test[0])]
    for i in range(2,test[0]+1):
      if 0<abs(test[i]-test[i-1])<test[0] and num[abs(test[i]-test[i-1])] == 0:
        num[abs(test[i]-test[i-1])] = 1
      else:
        case = False
    if case == True:
      print('Jolly')
    else:
      print('Not jolly')
  except:
    exit()