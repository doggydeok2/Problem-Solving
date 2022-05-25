import collections


N = int(input())
cars = collections.defaultdict(int)
q = collections.deque([])
cnt = 0
for _ in range(2 * N):
    car = input()
    if not cars[car]:
        cars[car] += 1
        q.append(car)
    else:
        cars[car] -= 1
        if q[0] == car:
            while q and cars[q[0]] == 0:
                q.popleft()
        else:
            cnt += 1
print(cnt)
