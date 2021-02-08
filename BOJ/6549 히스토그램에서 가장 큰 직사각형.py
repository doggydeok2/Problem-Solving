while True:
    h = list(map(int, input().split())) + [0]
    if len(h) == 2 and not h[0] and not h[1]:
        break
    s = [(0, 0) for _ in range(100000)]
    s[0] = (h[1], 1)
    maxSize = ptr = 0

    for i in range(2, h[0] + 2):
        inheritIndex = 0
        while s[ptr][0] > h[i] and ptr >= 0:
            maxSize = max(maxSize, s[ptr][0] * (i - s[ptr][1]))
            inheritIndex = s[ptr][1]
            ptr -= 1
        if ptr == -1 or h[i] > s[ptr][0]:
            ptr += 1
            s[ptr] = (h[i], inheritIndex if inheritIndex else i)
    print(maxSize)