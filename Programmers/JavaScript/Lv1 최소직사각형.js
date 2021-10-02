function solution(sizes) {
  const [ww, wh] = sizes.reduce((acc, size) => [Math.max(...size, acc[0]), Math.max(Math.min(...size), acc[1])], [0, 0]);
  return ww * wh;
}