function solution(a, b) {
  return a.map((val, idx) => val * b[idx]).reduce((acc, val) => acc + val);
  // reduce를 idx로 접근 시 map이 필요없음
  // return a.reduce((acc, val, idx) => acc + a[idx] * b[idx]);
}