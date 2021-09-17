function solution(x) {
  const backupX = x;
  let sumOfNum = 0;
  while (x) {
      sumOfNum += x % 10;
      x = Math.floor(x / 10);
  }
  return backupX % sumOfNum ? false : true;
}