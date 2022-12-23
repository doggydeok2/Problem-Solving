input()
clothes = list(map(int, input().split()))
men = sum(clothes)
if men == 1:
    print('Happy')
else:
    print(['Unhappy', 'Happy'][max(clothes) <= (men >> 1)])
