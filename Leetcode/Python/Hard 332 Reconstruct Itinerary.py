class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary_dict = collections.defaultdict(list)
        
        for ticket in sorted(tickets):
            start, end = ticket
            itinerary_dict[start].append(end)
        
        output = []
        
        def dfs(s):
            while itinerary_dict[s]:
                go_next = itinerary_dict[s].pop(0)
                dfs(go_next)
            output.append(s)
                
        dfs("JFK")
        return output[::-1]
                