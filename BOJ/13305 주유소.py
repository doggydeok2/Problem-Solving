N = int(input())
distance = list(map(int, input().split())) + [0]
gasPrice = list(map(int, input().split()))

cost = 0
minGasPrice = gasPrice[0]
for i in range(N):
    price = gasPrice[i]
    if minGasPrice > price:
        minGasPrice = price
    cost += minGasPrice * distance[i]
print(cost)
