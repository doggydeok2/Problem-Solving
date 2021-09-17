function solution(arr) {
  const sum = arr.reduce((acc, val) => {
      return acc + val;
  }, 0);
  return sum / arr.length;
}