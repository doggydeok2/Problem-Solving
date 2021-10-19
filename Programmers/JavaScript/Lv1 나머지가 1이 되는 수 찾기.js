function solution(n) {
  n -= 1;
  for (let i = 2; i <= n; i++) {
      if (n % i) continue;
      return i;
  }
  return n;
}