function solution(new_id) {
  let potentialID = (new_id
  .toLowerCase()
  .replace(/[^\w\-\.]/g, "")
  .replace(/\.{2,}/g, ".")
  .replace(/^\.|\.$/g, "") || "a")
  .slice(0, 15)
  .replace(/\.$/, "");
  
  while (potentialID.length < 3) potentialID += potentialID.slice(-1);
  
  return potentialID;
}