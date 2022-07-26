A, B = map(int, input().split())

sieve = [True] * (int(B ** 0.5) + 1)
sieve[0] = sieve[1] = False
for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0

cnt = 0
for idx, is_prime in enumerate(sieve):
    if not is_prime:
        continue
    val = idx ** 2
    while val <= B:
        if A <= val <= B:
            cnt += 1
        val *= idx
print(cnt)
