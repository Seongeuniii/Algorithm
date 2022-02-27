function solution(records) {
  let answer = [];
  const printer = {
    1: '님이 들어왔습니다.',
    0: '님이 나갔습니다.'
  }
  let kakao = [];
  let user = {};

  records.forEach( record => {
    r = record.split(' ');

    if (r[0] == 'Enter') {
      kakao.push([1, r[1]]);
      user[r[1]] = r[2];
    } else if (r[0] == 'Leave') {
      kakao.push([0, r[1]]);
    } else {
      user[r[1]] = r[2];
    }

  })

  kakao.forEach( k => {
    answer.push( String(user[k[1]]) + printer[k[0]] );
  })

  return answer;
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))