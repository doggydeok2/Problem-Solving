N, M = map(int, input().split())
nums = list(map(int, input().split()))
q = [i for i in range(1, N + 1)]
f = cnt = 0

for num in nums:
    i = 0
    l = len(q)
    while q[(f + i) % l] != num and q[(f - i) % l] != num:
        i += 1
    f = (f + i) % l if q[(f + i) % l] == num else (f - i) % l
    q.pop(f)
    cnt += i

print(cnt)
