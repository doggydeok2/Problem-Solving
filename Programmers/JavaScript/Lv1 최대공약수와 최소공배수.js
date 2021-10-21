function solution(n, m) {
  const minNum = Math.min(n, m),
        maxNum = Math.max(n, m);
  let gcd = 0,
      lcm = 0;
  
  for (let i = minNum; i > 0; i--) {
      if (!(n % i) && !(m % i)) {
          gcd = i;
          break;
      }
  }
  
  for (let i = maxNum; i <= (n * m); i++) {
      if (!(i % n) && !(i % m)) {
          lcm = i;
          break;
      }
  }
  
  return [gcd, lcm];
}