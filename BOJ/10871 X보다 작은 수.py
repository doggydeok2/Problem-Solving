N, X = map(int, input().split())
arr = list(map(int, input().split()))

for num in arr:
    if X > num:
        print(num, end=' ')
print()