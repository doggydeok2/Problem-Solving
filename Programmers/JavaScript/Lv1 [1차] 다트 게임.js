function solution(dartResult) {
  const score = [];
  
  let s = 0;
  for (let i = 0; i < dartResult.length; i++) {
      let cmd = dartResult[i]
      if (cmd === 'S' || cmd === 'D' || cmd === 'T') {
          let tempScore = parseInt(dartResult.slice(s, i));
          if (cmd === 'S') {
              score.push(tempScore)
          } else if (cmd === 'D') {
              score.push(tempScore ** 2)
          } else {
              score.push(tempScore ** 3)
          }
          s = i + 1
      } else if (cmd === '*') {
          score[score.length - 1] *= 2
          if (score.length > 1) {
              score[score.length - 2] *= 2
          }
          s = i + 1
      } else if (cmd === '#') {
          score[score.length - 1] *= -1
          s = i + 1
      }
  }
  return score.reduce((acc, val) => acc + val)
}