def find_gcd(a, b):
    if a < b:
        a, b = b, a
    c = a % b
    while c:
        b, c = c, b % c
    return b


N = int(input())
nums = [int(input()) for _ in range(N)]

gcd = abs(nums[1] - nums[0])
for i in range(2, N):
    gcd = find_gcd(gcd, abs(nums[i] - nums[i - 1]))

divisors = []
for i in range(2, int(gcd ** (1/2)) + 1):
    if not gcd % i:
        divisors.append(i)
        divisors.append(gcd // i)
divisors.append(gcd)

divisors = sorted(list(set(divisors)))
print(*divisors)