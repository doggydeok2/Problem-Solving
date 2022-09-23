ans, last = 0, '/'
for ch in input():
    ans += 5 + (last != ch) * 5
    last = ch
print(ans)
