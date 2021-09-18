function solution(n) {
  const sq = Math.sqrt(n);
  return sq % 1 ? -1 : (sq + 1) ** 2;
}