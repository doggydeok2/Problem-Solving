function solution(left, right) {
  let answer = 0;
  for (let i = left; i < right + 1; i++) {
      answer += (i ** 0.5) % 1 ? i : -i
  }
  return answer
}