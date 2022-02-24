function solution(s) {
  var answer = s.length;
  for (let cut = 1; cut < parseInt(s.length/2) + 1; cut++) {
    let result = 0
    let pattern = '';
    let cnt = 0;
    for (let i = 0; i < s.length; i += cut) {
      let newPattern = s.slice(i,i+cut);
      if (newPattern == pattern) {
        cnt += 1
      } else {
        result += newPattern.length
        if (cnt > 1) {
          result += String(cnt).length
        }
        pattern = newPattern
        cnt = 1
      }
    }
    if (cnt > 1) {
      result += String(cnt).length
    }
    answer = Math.min(answer, result)
  }
  return answer;
}