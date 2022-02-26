
function solution(s) {
  let answer = [];
  s = s.slice(2,-2).split('},{')

  for (let i=0; i<s.length; i++) {
    s[i] = s[i].split(',').map( x => Number(x))
  }

  s.sort((a,b) => a.length - b.length)

  for (let i=0; i<s.length; i++) {
    for (let j=0; j<s[i].length; j++) {
      if (!answer.includes(s[i][j])) {
        answer.push(s[i][j])
      }
    }
  }

  return answer;
}

console.log(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))