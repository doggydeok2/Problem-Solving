import sys
rl = sys.stdin.readline

N, M = map(int, rl().split())
passwords = {}

for _ in range(N):
    domain, pw = rl().split()
    passwords[domain] = pw

for _ in range(M):
    print(passwords[rl().rstrip()])
