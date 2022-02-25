function solution(rows, columns, queries) {
  let answer = [];

  let board = new Array(rows);
  for(let i = 0; i < rows; i++) {
    board[i] = new Array(columns);
    for(let j = 0; j < columns; j++) {
      board[i][j] = i*columns + (j+1)
    }
  }
  // const a = [...Array(rows)].map((_, r)=>[...Array(columns)].map((_, c)=>r*columns+c+1))

  queries.forEach((query) => {
    const [x1, y1, x2, y2] = query.map(q => q - 1)
    stack = [board[x1][y1]]

    for (let e = y1 + 1; e < y2 + 1; e++) {
      stack.push(board[x1][e])
      board[x1][e] = stack[stack.length-2]
    }

    for (let s = x1 + 1; s < x2 + 1; s++) {
      stack.push(board[s][y2])
      board[s][y2] = stack[stack.length-2]
    }

    for (let w = y2 - 1; w > y1 - 1; w--) {
      stack.push(board[x2][w])
      board[x2][w] = stack[stack.length-2]
    }

    for (let n = x2 - 1; n > x1 - 1; n--) {
      stack.push(board[n][y1])
      board[n][y1] = stack[stack.length-2]
    }
    answer.push(Math.min(...stack))
  })

  return answer;
}