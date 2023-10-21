n = int(input())
fibos = [0] * 46
fibos[1] = 1
for i in range(2, 46):
    fibos[i] = fibos[i - 1] + fibos[i - 2]
print(fibos[n])