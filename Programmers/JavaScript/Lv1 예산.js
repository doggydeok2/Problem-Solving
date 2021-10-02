function solution(d, budget) {
  return d.sort((a, b) => a - b).reduce((acc, cur) => {
      budget -= cur;
      return acc + (budget >= 0);
  }, 0);
}