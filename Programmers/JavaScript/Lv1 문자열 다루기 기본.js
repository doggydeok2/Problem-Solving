function solution(s) {
  if (s.length !== 4 && s.length !== 6) return false;
  
  for (let ch of s) {
      if ("0123456789".indexOf(ch) === -1) return false;
  }
  
  return true;
}