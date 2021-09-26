function solution(n) {
  let answer = 0;
  for (let i = 1; i <= Math.floor(Math.sqrt(n)); i++) {
      answer += n % i ? 0 : i + n / i - (i === n / i && i);
  }
  return answer;
}