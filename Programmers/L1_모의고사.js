function solution(answers) {
  let answer = [];

  const students = [
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ];
  let scores = Array.from({length: students.length}, () => 0);

  // answers.forEach((ans, i) => {
  //   students.forEach((std, j) => {
  //     if (ans == std[i % std.length]) {
  //       scores[j] += 1;
  //     };
  //   });
  // });

  students.forEach((std, j) => {
    scores[j] = answers.filter((ans, i) => ans == std[i % std.length]).length;
  })

  const S = Math.max(...score);
  scores.forEach((s, n) => {
    if (s == S) {
      answer.push(n+1);
    };
  });

  return answer;
}