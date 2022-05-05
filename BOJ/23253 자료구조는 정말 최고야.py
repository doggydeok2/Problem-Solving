import sys
rl = sys.stdin.readline


def able_to_sort():
    N, M = map(int, rl().split())
    for i in range(M):
        l = int(rl())
        books = list(map(int, rl().split()))
        for j in range(1, l):
            if books[j - 1] < books[j]:
                return 'No'
    return 'Yes'

print(able_to_sort())
