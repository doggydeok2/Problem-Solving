H, W = map(int, input().split())
heights = list(map(int, input().split()))
left_highest, right_highest = [0] * W, [0] * W
left_highest[0], right_highest[-1] = heights[0], heights[-1]
for i in range(1, W):
    left_highest[i] = max(left_highest[i - 1], heights[i])
    right_highest[-(i + 1)] = max(right_highest[-i], heights[-(i + 1)])
print(sum([min(left_highest[i], right_highest[i]) - heights[i] for i in range(W)]))
