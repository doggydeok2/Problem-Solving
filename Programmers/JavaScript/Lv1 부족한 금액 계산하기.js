function solution(price, money, count) {
  const shortage = price * count * (count + 1) / 2 - money;
  return shortage > 0 ? shortage : 0;
}