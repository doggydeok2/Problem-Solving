A, B, C = map(int, input().split())
N = int(input())

team_score = max_team_score = 0
for i in range(N):
    team_score = 0
    for j in range(3):
        A_freq, B_freq, C_freq = map(int, input().split())
        team_score += A_freq * A + B_freq * B + C_freq * C
    max_team_score = max(max_team_score, team_score)
print(max_team_score)