W = input()
ans = 0
for ch in W:
    if ch == 'A':
        ans += 1
print(f'{ans} : {len(W) - ans}')
