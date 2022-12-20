N = int(input())
friends = [[] for _ in range(N + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0] * (N + 1)
for friend in friends[1]:
    visited[friend] = 1
    for another in friends[friend]:
        visited[another] = 1
print(visited.count(1) - visited[1])
