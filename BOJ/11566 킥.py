def checking(start, gap):
    x = 0
    for i in range(start, m, gap):
        if x == n:
            return 1
        elif songs[i] != melodies[x]:
            return 0
        x += 1
    if x == n:
        return 1


n = int(input())
melodies = list(map(int, input().split()))
m = int(input())
songs = list(map(int, input().split()))
minDream = maxDream = -1

for s in range(m):
    if songs[s] != melodies[0]:
        continue

    for g in range(1, m - s):
        if songs[s + g] != melodies[1]:
            continue

        if checking(s, g):
            if minDream == -1 or minDream > g - 1:
                minDream = g - 1
            if maxDream < g - 1:
                maxDream = g - 1

if minDream == -1:
    print(-1)
else:
    print(minDream, maxDream)
