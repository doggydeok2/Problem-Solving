function solution(x, n) {
  const answer = new Array(n).fill(0);
  return answer.map((val, idx) => x * (idx + 1));
}