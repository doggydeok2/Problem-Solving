a, b = map(int, input().split())
min_gap = abs(b - a)
while min_gap and min_gap % 2 == 0:
    min_gap //= 2
for _ in range(5):
    p, q = map(int, input().split())
    pq_gap = abs(q - p)
    if min_gap == pq_gap == 0:
        print('Y')
    elif a > b and p < q or a < b and p > q:
        print('N')
    elif (min_gap and not pq_gap) or (not min_gap and pq_gap):
        print('N')
    elif min_gap % pq_gap and pq_gap % min_gap:
        print('N')
    else:
        print('Y')
