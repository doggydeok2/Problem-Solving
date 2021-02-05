n, w, L = map(int, input().split())
a = list(map(int, input().split()))

curL = ptr = truckArrived = 0
bridge = [0] * w
f, r, t = 0, w - 1, 1

while truckArrived < n:
    if ptr < n and curL + a[ptr] <= L:
        bridge[r] = a[ptr]
        curL += bridge[r]
        ptr += 1
    if bridge[f]:
        truckArrived += 1
        curL -= bridge[f]
        bridge[f] = 0
    f = (f + 1) % w
    r = (r + 1) % w
    t += 1

print(t)
