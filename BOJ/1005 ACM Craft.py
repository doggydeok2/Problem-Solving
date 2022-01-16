import collections
import sys
rl = sys.stdin.readline


T = int(rl())
for tc in range(T):
    N, K = map(int, rl().split())
    building_times = [0] + list(map(int, rl().split()))
    acc_times = [0] * (N + 1)
    able_do_next = [[] for _ in range(N + 1)]
    topology_arr = [0] * (N + 1)

    for i in range(K):
        s, e = map(int, rl().split())
        able_do_next[s].append(e)
        topology_arr[e] += 1

    W = int(rl())
    q = collections.deque([])
    for i in range(1, N + 1):
        if topology_arr[i] == 0:
            q.append(i)

    while q:
        popped_idx = q.popleft()
        acc_time = building_times[popped_idx] + acc_times[popped_idx]
        for do_next in able_do_next[popped_idx]:
            acc_times[do_next] = max(acc_times[do_next], acc_time)
            topology_arr[do_next] -= 1
            if topology_arr[do_next] == 0:
                q.append(do_next)

    print(acc_times[W] + building_times[W])
