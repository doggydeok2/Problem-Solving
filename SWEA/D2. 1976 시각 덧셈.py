T = int(input())
for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h1 += h2
    m1 += m2
    if m1 >= 60:
        h1 += 1
        m1 -= 60
    if h1 > 12:
        h1 -= 12
    print(f'#{tc} {h1} {m1}')