N = int(input())
heights = list(map(int, input().split()))
ans = [0] * N
stack = []
for idx, height in enumerate(heights):
    while stack and heights[stack[-1]] < height:
        stack.pop()
    ans[idx] = stack[-1] + 1 if stack else 0
    stack.append(idx)
print(*ans)
