N = int(input())
homes = sorted(list(map(int, input().split())))
min_dist, min_dist_home = 1e10, 0

left_sum, right_sum = 0, sum(homes)
for idx, home in enumerate(homes):
    right_sum -= home
    temp_dist = home * idx - left_sum + right_sum - home * (len(homes) - idx - 1)
    left_sum += home

    if min_dist > temp_dist:
        min_dist, min_dist_home = temp_dist, home

print(min_dist_home)

# 중앙값이 최소 - 항상 성립
# N = int(input())
# print(sorted(list(map(int, input().split())))[(N - 1) // 2])
