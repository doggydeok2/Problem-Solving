function solution(participant, completion) {
  const cntMap = new Map();
  participant.forEach(el => cntMap.set(el, cntMap.has(el) ? cntMap.get(el) + 1 : 1));
  completion.forEach(el => {
    cntMap.set(el, cntMap.get(el) - 1);
    if (cntMap.get(el) === 0) cntMap.delete(el);
  });
  for (let [key, val] of cntMap) {
    return key;
  }
}