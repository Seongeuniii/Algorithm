# 문제 설명
# 자연수 n과 시계/반시계 방향을 결정하는 boolean 값 clockwise가 주어진다.
# 소용돌이 모양(clockwise가 참이면 시계방향, 거짓이면 반시계방향)으로 n x n 정수 배열을 채워 return 해야한다.
# 제한사항
# 1 <= n <= 1000

# 입출력 예
# 5	True	
# [[1,2,3,4,1],
#  [4,5,6,5,2],
#  [3,6,7,6,3],
#  [2,5,6,5,4],
#  [1,4,3,2,1]]
# 6	False	,
# [[1,5,4,3,2,1],
#  [2,6,8,7,6,5],
#  [3,7,9,9,8,4],
#  [4,8,9,9,7,3],
#  [5,6,7,8,6,2],
#  [1,2,3,4,5,1]]

def solution(n, clockwise):
  answer = [[0]*n for _ in range(n)]

  # 방향 설정
  if clockwise:
    dx, dy = [0,1,0,-1], [1,0,-1,0]

  else:
    dx, dy = [1,0,-1,0], [0,1,0,-1]

  s = 1
  x, y = 0, 0

  while n > 0 :
    nums = [i for i in range(s, s + n)]

    for i in range(4):
      answer[x][y] = nums[0]

      if len(nums) == 1:
        break

      for j in range(1, len(nums) - 1):
        x, y = x+dx[i], y+dy[i]
        answer[x][y] = nums[j]

      x, y = x+dx[i], y+dy[i]
      
    x, y = x+1, y+1
    s += (n-1)
    n -= 2

  return answer

print(solution(1, False))