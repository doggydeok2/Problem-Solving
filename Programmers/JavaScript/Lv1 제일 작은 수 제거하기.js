function solution(arr) {
  if (arr.length === 1) return [-1];
  arr.splice(arr.findIndex(el => el === Math.min(...arr)), 1);
  return arr;
}