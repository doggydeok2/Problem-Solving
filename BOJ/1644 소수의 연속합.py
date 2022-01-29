def move_ptr(_x, _max):
    while _x < _max and sieve[_x] == 0:
        _x += 1
    return _x


N = int(input())
sieve = [1] * (N + 1)
sieve[0] = sieve[1] = 0

for n in range(2, N + 1):
    if sieve[n] == 1:
        k = n
        n += k
        while n <= N:
            sieve[n] = 0
            n += k

left = right = acc = 2
cnt = 0
while left <= right <= N:
    if acc > N:
        acc -= left
        left = move_ptr(left + 1, N + 1)
    else:
        if acc == N:
            cnt += 1
        right = move_ptr(right + 1, N + 1)
        if right != N + 1:
            acc += right
print(cnt)
