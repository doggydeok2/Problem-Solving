function solution(n) {
  let left = 1,
      right = 1,
      sum = 1,
      cnt = 0;
  
  while (left <= right) {
      if (sum >= n) {
          if (sum === n) cnt += 1;
          sum -= left;
          left += 1;
      } else {
          right += 1;
          sum += right;
      }
  }
  
  return cnt;
}