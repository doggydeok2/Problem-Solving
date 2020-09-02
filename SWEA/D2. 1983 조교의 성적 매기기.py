T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grades = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    scores = [0] * N
    for i in range(N):
        scores[i] = list(map(int, input().split()))
        scores[i] = 0.35 * scores[i][0] + 0.45 * scores[i][1] + 0.2 * scores[i][2]

    scoresSorting = scores[:]
    scoresSorting.sort()
    
    for i in range(N):
        scores[i] = scoresSorting.index(scores[i])
        scores[i] = grades[scores[i] * 10 // N]
        
    print(f'#{tc} {scores[K - 1]}')