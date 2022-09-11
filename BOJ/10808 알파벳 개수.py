ans = [0] * 26
for ch in input():
    ans[ord(ch) - 97] += 1
print(*ans)
