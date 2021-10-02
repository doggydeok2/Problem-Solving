function solution(arr, divisor) {
  const filteredArray = arr.filter(val => !(val % divisor)).sort((a, b) => a - b);
  return filteredArray.length ? filteredArray : [-1];
}