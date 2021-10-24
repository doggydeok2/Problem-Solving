function solution(s) {
  const numWords = [
      "zero", "one", "two", "three", "four",
      "five", "six", "seven", "eight", "nine"
  ];
  
  numWords.forEach((num, idx) => {
      const regex = new RegExp(num, 'g');
      s = s.replace(regex, idx.toString());
  })
  
  return parseInt(s)
}