def solution(rows, columns, queries):
  answer = []
  board = [[(r*columns+c) for c in range(1, columns + 1)] for r in range(rows)]

  for x1, y1, x2, y2 in queries:
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    stack = [board[x1][y1]]

    for e in range(y1+1, y2+1):
      stack.append(board[x1][e])
      board[x1][e] = stack[-2]

    for s in range(x1+1, x2+1):
      stack.append(board[s][y2])
      board[s][y2] = stack[-2]

    for w in range(y2-1, y1-1, -1):
      stack.append(board[x2][w])
      board[x2][w] = stack[-2]

    for n in range(x2-1, x1-1, -1):
      stack.append(board[n][y1])
      board[n][y1] = stack[-2]

    answer.append(min(stack))

  return answer