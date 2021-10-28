function solution(n) {
  const fibo = [1, 1, 2];
  
  for (let i = 2; i < n; i++) {
      fibo[i % 3] = (fibo[(i + 1) % 3] + fibo[(i + 2) % 3]) % 1234567;
  }
  return fibo[(n - 1) % 3];
}