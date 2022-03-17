# 문제 설명
# 가로 1칸, 세로 1칸의 크기를 갖는 정사각형으로 이루어진 가로 width칸, 세로 height칸의 격자가 있다.
# 일부 정사각형에는 "왼쪽 위의 점과 오른쪽 아래점을 잇는" 대각선이 있다.
# 이 격자에서 대각선을 정확히 1번 이용해, 좌측 하단의 끝점에서 우측 상단의 끝점으로 가는 최단거리 경로를 구해야 한다.

# 입력
# width: 격자의 가로 길이
# height: 격자의 세로 길이
# diagonals: 대각선이 위치한 정사각형의 정보

# 출력
# 주어진 조건을 모두 만족하는 경로의 개수를 10,000,019로 나눈 나머지를 return

# 제한사항
# 1 ≤ width ≤ 250
# 1 ≤ height ≤ 250
# 1 ≤ diagonals의 길이 ≤ width × height
# diagonals의 각 행은 두 정수 [x, y]로 이루어져 있으며, 왼쪽에서부터 x번째, 아래에서부터 y번째 사각형에 대각선이 있음을 의미합니다.
# 1 ≤ x ≤ width
# 1 ≤ y ≤ height
# 똑같은 (x, y) 순서쌍은 2번 이상 등장하지 않습니다.

# 입출력 예
# 2	2	[[1,1],[2,2]]	12
# 51	37	[[17,19]]	3225685 (실제 경우의 수는 776,469,491,667,984,972,858,000 가지)

from collections import deque

def solution(W, H, diagonals):
  dp = [[[0, 0] for _ in range(W+1)] for _ in range(H+1)]
  dgn = [[[0, 0] for _ in range(W+1)] for _ in range(H+1)]

  for gx, gy in diagonals:
    dgn[H-gy][gx-1][0] = 1
    dgn[H-(gy-1)][gx][1] = 1

  dx, dy = [-1, 0], [0, 1]

  q = deque([(H, 0)])
  dp[H][0] = [1, 0]

  while q:
    iq = q
    s = set()
    
    while iq:
      x, y = iq.popleft()

      if dgn[x][y][0]:
        dp[x][y][1] += dp[x+1][y+1][0]

      if dgn[x][y][1]:
        dp[x][y][1] += dp[x-1][y-1][0]

      for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<=H and 0<=ny<=W:
          dp[nx][ny][0] += dp[x][y][0]
          dp[nx][ny][1] += dp[x][y][1]
          s.add((nx, ny))
        
    q = deque(list(s))
  
  return dp[0][W][1] % 10000019

print(solution(51,	37,	[[17,19]]))