N = int(input())
scores = [[0, 0] for _ in range(N)]
scores[0][0] = scores[0][1] = int(input())
if N > 1:
    scores[1][0] = int(input())
    scores[1][1] = scores[0][0] + scores[1][0]

for i in range(2, N):
    score = int(input())
    scores[i][0], scores[i][1] = max(scores[i - 2]) + score, scores[i - 1][0] + score

print(max(scores[-1]))