N = int(input())
left = list(map(int, input().split()))
order = []

for i in range(1, N + 1):
    if len(order) <= left[-i]:
        order.append(N - i + 1)
    else:
        order.insert(left[-i], N - i + 1)
print(*order)
