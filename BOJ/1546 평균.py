N = int(input())
scores = list(map(int, input().split()))
scMax = max(scores)
for i in range(N):
    scores[i] = scores[i] / scMax * 100
print(sum(scores) / N)