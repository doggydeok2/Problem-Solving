s, e = map(int, input().split())
length = int(e ** 0.5) + 1

sieve = [True] * length
sieve[0] = sieve[1] = False
for i in range(2, length):
    if not sieve[i]:
        continue
    nxt = i * 2
    while nxt < length:
        sieve[nxt] = False
        nxt += i

arr = [True] * (e - s + 1)
for i in range(2, length):
    if not sieve[i]:
        continue
    i_sq = i ** 2
    nxt = i_sq - s % i_sq if s % i_sq else 0
    while nxt <= e - s:
        arr[nxt] = False
        nxt += i_sq
print(arr.count(True))
