function solution(n, lost, reserve) {
  const owner = new Array(n + 1).fill(1);
  lost.forEach(el => owner[el] = 0);
  reserve.forEach(el => owner[el] += 1);
  
  return owner.reduce((acc, cur, idx) => {
      if (idx === n && cur > 1 ||
          owner[idx - 1] > 1 && !owner[idx]) cur = 1
      else if (owner[idx + 1] > 1 && !owner[idx]) {
          owner[idx + 1] -= 1;
          cur = 1
      }
      
      return acc + !!cur
  }, 0) - 1;
}