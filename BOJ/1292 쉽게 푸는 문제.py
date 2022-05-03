arr = [0]
for i in range(46):
    arr.extend([i] * i)
s, e = map(int, input().split())
print(sum(arr[s:e + 1]))
