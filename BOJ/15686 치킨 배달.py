import itertools


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
chicken_house = []
house = []

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            house.append((i, j))
        elif data[i][j] == 2:
            chicken_house.append((i, j))
        # else do nothing

distance_table = [[0] * len(chicken_house) for _ in range(len(house))]
for i in range(len(house)):
    house_y, house_x = house[i]
    for j in range(len(chicken_house)):
        chicken_y, chicken_x = chicken_house[j]
        distance_table[i][j] = abs(chicken_x - house_x) + abs(chicken_y - house_y)

INF = 1e4
min_chicken_distance = INF
for selects in itertools.combinations([i for i in range(len(chicken_house))], M):
    temp_distance = 0
    for i in range(len(house)):
        min_dist = INF
        for j in selects:
            min_dist = min(min_dist, distance_table[i][j])
        temp_distance += min_dist
    min_chicken_distance = min(min_chicken_distance, temp_distance)

print(min_chicken_distance)
