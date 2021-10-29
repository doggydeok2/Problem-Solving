function solution(arr) {
  return arr.reduce((acc, cur) => {
      const [smaller, bigger] = acc > cur ? [cur, acc] : [acc, cur];
      let i = smaller;
      while (true) {
          if (i % bigger) i += smaller;
          else return i;
      }
  });
}