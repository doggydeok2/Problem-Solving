N, M = map(int, input().split())
H = list(map(int, input().split()))
totHappiness = sum(H)
totBlue = 0
feelBadDays = M - totHappiness - N

i = 0
while i < feelBadDays:
    totBlue += (1 + i // (N + 1)) ** 2
    i += 1
print(totBlue)