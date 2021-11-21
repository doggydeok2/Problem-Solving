class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer, stack = [0] * len(temperatures), [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                lower = stack.pop()
                answer[lower] = i - lower
            stack.append(i)
        return answer

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer, stack = [0] * len(temperatures), [0]
#         for i, cur in enumerate(temperatures):
#             while stack and temperatures[stack[-1]] < cur:
#                 lower = stack.pop()
#                 answer[lower] = i - lower
#             stack.append(i)
#         return answer
                