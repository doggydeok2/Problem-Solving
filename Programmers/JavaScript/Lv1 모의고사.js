function solution(answers) {
  const marking = [
      [1, 2, 3, 4, 5],
      [2, 1, 2, 3, 2, 4, 2, 5],
      [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ];
  const len = answers.length;
  const score = [0, 0, 0];
  
  for (let i = 0; i < 3; i++) {
      let l = marking[i].length;
      score[i] = answers.reduce((acc, val, idx) => {
          return acc + (marking[i][idx % l] === val)
      }, 0);
  }
  
  let maxScore = score[0];
  let maxScoreList = [1];
  
  for (let i = 1; i < 3; i++) {
      if (maxScore === score[i]) maxScoreList.push(i + 1);
      else if (maxScore < score[i]) {
          maxScore = score[i];
          maxScoreList = [i + 1];
      } 
  }
  
  return maxScoreList;
}