class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = collections.Counter(nums).most_common(k)
        return [obj[0] for obj in freq_dict]