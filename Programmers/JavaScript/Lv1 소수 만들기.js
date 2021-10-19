function isPrime(num) {
  const r = Math.ceil(Math.sqrt(num));
  for (let i = 2; i <= r; i++)
      if (!(num % i)) return false;
  return true;
}


function solution(nums) {
  const numLen = nums.length;
  let cnt = 0;

  for (let i = 0; i < numLen - 2; i++)
      for (let j = i + 1; j < numLen - 1; j++)
          for (let k = j + 1; k < numLen; k++)
              cnt += isPrime(nums[i] + nums[j] + nums[k]);
  
  return cnt;
}