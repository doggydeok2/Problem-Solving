class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        idx = fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]:
                fuel = 0
                idx = i + 1
            else:
                fuel += gas[i] - cost[i]
        return idx
    