class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])
        
        ans = []
        while heap:
            person = heapq.heappop(heap)
            ans.insert(person[1], [-person[0], person[1]])
        return ans
