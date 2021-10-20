function isPrime(n) {
  for (let i = 2; i <= n ** 0.5; i++)
      if (!(n % i)) return false;
  return true;
}


function solution(n) {
  const chkArr = new Array(n + 1).fill(1);
  
  for (let i = 2; i <= n ** 0.5; i++) {
      if (chkArr[i] && isPrime(i)) {
          for (let j = i * 2; j <= n; j += i)
              chkArr[j] = 0
      }
  }
  return chkArr.filter(n => n).length - 2;
}