def solution(N, exp):
  op = ['+', '-', '*']

  numList = []
  opList = []

  for e in exp:
    if e in op:
      opList.append(e)
    else:
      numList.append(e)

  dp = [(0,0)]*len(numList)
  dp[0] = (numList[0], numList[0])
  dp[1] = (str(eval(numList[0]+opList[0]+numList[1])), str(eval(numList[0]+opList[0]+numList[1])))

  for i in range(2, len(numList)):
    case = [
    eval(dp[i-2][0] + opList[i-2] + str(eval(numList[i-1]+opList[i-1]+numList[i]))),
    eval(dp[i-2][1] + opList[i-2] + str(eval(numList[i-1]+opList[i-1]+numList[i]))),
    eval(dp[i-1][0] + opList[i-1] + numList[i]),
    eval(dp[i-1][1] + opList[i-1] + numList[i]),
    ]

    dp[i] = (str(min(case)), str(max(case)))

  return max(int(dp[-1][0]), int(dp[-1][1]))

N = int(input())
exp = input().strip()
if N == 1:
  print(exp)
else:
  print(solution(N, exp))