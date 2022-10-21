ans = 0
for n in input():
    ans += int(n)
    if n == '0':
        ans += 9
print(ans)
