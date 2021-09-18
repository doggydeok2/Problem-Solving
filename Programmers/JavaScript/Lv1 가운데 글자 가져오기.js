function solution(s) {
  const l = s.length, m = Math.floor(l / 2);
  return l % 2 ? s.slice(m, m + 1) : s.slice(m - 1, m + 1);
}