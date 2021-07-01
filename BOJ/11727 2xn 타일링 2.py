n = int(input())
counting = [0] * max(3, n + 1)
counting[1], counting[2] = 1, 3

for i in range(3, n + 1):
    counting[i] = (counting[i - 1] + 2 * counting[i - 2]) % 10007

print(counting[n])
