string = input()
R_total = string.count('R')
ans = R_total
lp, rp, lk, rk = 0, len(string) - 1, string[0] == 'K', string[-1] == 'K'

while lp <= rp:
    if string[lp] == 'R':
        ans = max(ans, min(lk, rk) * 2 + R_total)
    if string[rp] == 'R':
        ans = max(ans, min(lk, rk) * 2 + R_total)
    if lk >= rk:
        R_total -= string[rp] == 'R'
        rp -= 1
        rk += string[rp] == 'K'
    else:
        R_total -= string[lp] == 'R'
        lp += 1
        lk += string[lp] == 'K'
print(ans)
