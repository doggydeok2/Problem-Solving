cups = [0, 1, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]
print(cups.index(1))
