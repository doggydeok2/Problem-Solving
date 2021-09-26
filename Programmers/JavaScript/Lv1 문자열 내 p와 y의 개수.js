function solution(s){
  return s.split("").reduce((acc, cur) => acc + (cur === "p" || cur === "P") - (cur === "y" || cur === "Y"), 0) === 0
}