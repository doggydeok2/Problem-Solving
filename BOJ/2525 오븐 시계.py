h, m = map(int, input().split())
t = h * 60 + m + int(input())
print(f'{t // 60 % 24} {t % 60}')
