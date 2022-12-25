input()
ans = set(map(int, input().split())) - set(map(int, input().split()))
print(len(ans))
print(*sorted(list(ans)))
