N, M = map(int, input().split())
Pi = sorted([int(input()) for _ in range(M)])
max_price = max_profit = 0
for i in range(M):
    temp_profit = Pi[i] * min(M - i, N)
    if max_profit < temp_profit:
        max_profit = temp_profit
        max_price = Pi[i]
print(max_price, max_profit)
