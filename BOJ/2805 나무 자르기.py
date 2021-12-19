import sys
rl = sys.stdin.readline

N, M = map(int, rl().rstrip().split())
trees = list(map(int, rl().rstrip().split()))
left, mid, right = 0, 0, 2000000000
max_len = 0

while left <= right:
    mid = (left + right) // 2
    get_tree = sum(tree - mid if tree > mid else 0 for tree in trees)

    if get_tree < M:
        right = mid - 1
    else:
        max_len = mid
        left = mid + 1

print(max_len)