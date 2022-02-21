let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const topList = input[1].split(' ')
const stack = []
const answer = []

for (let i = 0; i < N; i++) {
  while (stack.length) {
    if (Number(topList[stack[stack.length-1]]) >= Number(topList[i])) {
      break
    } else {
      stack.pop()
    }
  }

  if (stack.length) {
    answer.push(stack[stack.length-1] + 1)
  } else {
    answer.push(0)
  }

  stack.push(i)
}

console.log(answer.join(' '))