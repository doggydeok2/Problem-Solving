prime = [i for i in range(10001)]
prime[1] = 0
for i in range(2, 9998):
    if prime[i]:
        j = 2
        while j * i <= 10000:
            prime[j * i] = 0
            j += 1

for tc in range(int(input())):
    n = int(input())
    nh = n // 2
    for x in range(nh):
        if prime[nh + x] and prime[nh - x]:
            print(prime[nh - x], prime[nh + x])
            break