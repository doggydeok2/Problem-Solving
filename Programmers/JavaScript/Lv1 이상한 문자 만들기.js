function solution(s) {
  const words = s.split(" ");
  let answer = "";
  for (let word of words) {
      for(let idx in word) {
          answer += idx % 2 ? word[idx].toLowerCase() : word[idx].toUpperCase();
      }
      answer += " ";
  }
  return answer.slice(0, -1);
}