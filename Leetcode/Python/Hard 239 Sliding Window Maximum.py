class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        
        for i, v in enumerate(nums):
            heapq.heappush(heap, (-v, i))
            if i < k - 1:
                continue
            while heap[0][1] + k <= i:
                heapq.heappop(heap)

            ans.append(-heap[0][0])
            
        return ans
