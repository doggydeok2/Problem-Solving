WEEKS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
week = 1

for m in range(1, 13):
    if x == m: break
    week += DAYS[m - 1]
week = (week + y - 1) % 7
print(WEEKS[week])