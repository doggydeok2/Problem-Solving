function solution(n) {
  const cntArr = new Array(10).fill(0);
  let answer = "";
  
  while (n) {
      cntArr[n % 10]++;
      n = Math.floor(n / 10);
  }
  
  for (let i = 9; i >= 0; i--) {
      answer += String(i).repeat(cntArr[i]);
  }
  
  return parseInt(answer);
}