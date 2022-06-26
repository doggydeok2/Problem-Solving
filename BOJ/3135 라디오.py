A, B = map(int, input().split())
N = int(input())
added = [int(input()) for _ in range(N)]
print(min(abs(A - B), min([abs(added[i] - B) + 1 for i in range(N)])))
