function solution(phone_number) {
  const cutline = phone_number.length - 4;
  
  return "*".repeat(cutline) + phone_number.slice(cutline);
}