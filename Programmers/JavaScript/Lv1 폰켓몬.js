function solution(nums) {
  const cntMap = new Set(nums);
  const halfLenNums = nums.length / 2,
        mapSize = cntMap.size;
  return halfLenNums > mapSize ? mapSize : halfLenNums;
}