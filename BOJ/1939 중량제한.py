import collections


def check_existed_bridge(start, end):
    for idx, bridge in enumerate(bridge_dict[start]):
        if end == bridge[0]:
            return idx
    return -1


def insert_bridge_to_dict(start, end, weight):
    existed_bridge_idx = check_existed_bridge(start, end)
    if existed_bridge_idx >= 0:
        bridge_dict[start][existed_bridge_idx][1] = max(bridge_dict[start][existed_bridge_idx][1], weight)
    else:
        bridge_dict[start].append([end, weight])


N, M = map(int, input().split())
visited = [0] * (N + 1)
bridge_dict = collections.defaultdict(list)

for _ in range(M):
    s, e, w = map(int, input().split())
    insert_bridge_to_dict(s, e, w)
    insert_bridge_to_dict(e, s, w)

S, E = map(int, input().split())
visited[S] = 1000000000
max_weight = 0
Q = collections.deque([[S, visited[S]]])
while Q:
    popped_island, popped_weight = Q.popleft()
    if popped_island == E:
        max_weight = max(popped_weight, max_weight)
    elif popped_weight < visited[popped_island]:
        pass
    else:
        for next_island, bridge_weight in bridge_dict[popped_island]:
            able_weight = min(popped_weight, bridge_weight)
            if visited[next_island] < able_weight:
                visited[next_island] = min(popped_weight, bridge_weight)
                Q.append([next_island, visited[next_island]])

print(max_weight)
