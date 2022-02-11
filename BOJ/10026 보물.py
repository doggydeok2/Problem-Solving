N = int(input())
A, B = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())), reverse=True)
print(sum([A[i] * B[i] for i in range(N)]))
