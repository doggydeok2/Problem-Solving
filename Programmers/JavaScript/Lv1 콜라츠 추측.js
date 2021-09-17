function solution(num) {
  let cnt = 0;
  while (num !== 1 && cnt <= 500) {
      num = num % 2 ? num * 3 + 1 : num / 2
      cnt += 1;
  }
  return cnt >= 500 ? -1 : cnt;
}