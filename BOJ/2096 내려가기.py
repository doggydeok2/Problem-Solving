import sys
rl = sys.stdin.readline


N = int(rl())
minA, minB, minC = map(int, rl().split())
maxA, maxB, maxC = minA, minB, minC
for t in range(1, N):
    A, B, C = map(int, rl().split())
    minA, maxA, minB, maxB, minC, maxC = \
        A + min(minA, minB), A + max(maxA, maxB), B + min(minA, minB, minC), \
        B + max(maxA, maxB, maxC), C + min(minB, minC), C + max(maxB, maxC)
print(max(maxA, maxB, maxC), min(minA, minB, minC))
