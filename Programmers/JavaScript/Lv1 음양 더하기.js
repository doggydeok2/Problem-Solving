function solution(absolutes, signs) {
  return absolutes.reduce((acc, absolute, idx) => acc + (signs[idx] ? 1 : -1) * absolute, 0);
}