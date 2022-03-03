function solution(priorities, location) {
  let answer = 0;
  let queue = priorities.map((p, i) => { return [i, p]});
  priorities.sort((a, b) => a - b);

  while (queue) {
    let [i, q] = queue.shift();
    p = priorities.pop();

    if (p > q) {
      queue.push([i, q]);
      priorities.push(p);
    } else {
      answer += 1
      if (i == location) {
        return answer;
      };
    };
  };
}
