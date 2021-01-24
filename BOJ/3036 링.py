def find_gcd(a, b):
    if a < b:
        a, b = b, a
    c = a % b
    while c:
        b, c = c, b % c
    return b


N = int(input())
rings = list(map(int, input().split()))

for i in range(1, N):
    gcd = find_gcd(rings[0], rings[i])
    print(f'{rings[0]//gcd}/{rings[i]//gcd}')