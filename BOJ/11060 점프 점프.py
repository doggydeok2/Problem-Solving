N = int(input())
nums = list(map(int, input().split()))
visited = [-1] * N
visited[0] = 0
q = [0]

for n in q:
    for i in range(n + 1, n + nums[n] + 1):
        if 0 <= i < N and visited[i] == -1:
            q.append(i)
            visited[i] = visited[n] + 1
print(visited[-1])
