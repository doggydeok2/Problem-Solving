P = [list(map(int, input().split())) for _ in range(3)]
ccw = P[0][0] * P[1][1] + P[1][0] * P[2][1] + P[2][0] * P[0][1] -\
      P[1][0] * P[0][1] - P[2][0] * P[1][1] - P[0][0] * P[2][1]
print(-1 if ccw < 0 else 0 if ccw == 0 else 1)
