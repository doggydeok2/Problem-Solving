function solution(n) {
  let triad = "";
  let decimal = 0;
  
  while (n) {
      triad += String(n % 3);
      n = Math.floor(n / 3);
  }
  
  const l = triad.length - 1;
  
  for (let i = l; i >= 0; i--) {
      decimal += parseInt(triad[i]) * (3 ** (l - i));
  }
  
  return decimal;
}

// parseInt([...n.toString(3)].reverse().join(""), 3);