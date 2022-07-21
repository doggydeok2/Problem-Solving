N = int(input())
topologies = [0] * (N + 1)
latecomers = [[] for _ in range(N + 1)]
times = [0] * (N + 1)
total_times = [0] * (N + 1)
for i in range(1, N + 1):
    i_info = list(map(int, input().split()))
    times[i] = i_info[0]
    for first_mover in i_info[1:-1]:
        topologies[i] += 1
        latecomers[first_mover].append(i)

building_queue = []
for i in range(1, N + 1):
    if topologies[i] == 0:
        building_queue.append(i)

for building in building_queue:
    total_times[building] += times[building]
    for latecomer in latecomers[building]:
        total_times[latecomer] = max(total_times[latecomer], total_times[building])
        topologies[latecomer] -= 1
        if topologies[latecomer] == 0:
            building_queue.append(latecomer)

for i in range(1, N + 1):
    print(total_times[i])
