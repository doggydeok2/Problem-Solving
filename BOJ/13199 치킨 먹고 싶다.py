import sys
rl = sys.stdin.readline


for tc in range(int(rl())):
    P, M, F, C = map(int, rl().split())
    cp, gap = C * (M // P), F - C
    print(1 + (cp - F) // gap - (cp // F) if cp >= F else 0)
