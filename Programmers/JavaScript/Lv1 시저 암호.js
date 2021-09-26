function solution(s, n) {
  const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const lower = "abcdefghijklmnopqrstuvwxyz";
  let answer = '';

  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') answer += ' ';
    else {
      let UTFCode = s.charCodeAt(i);
      answer += UTFCode > 96
      ? lower[(UTFCode + n - 97) % 26]
      : upper[(UTFCode + n - 65) % 26];
    }
  }
  return answer;
}