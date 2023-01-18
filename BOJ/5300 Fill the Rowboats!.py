ans = []
for i in range(1, int(input()) + 1):
    ans.append(i)
    if i % 6 == 0:
        ans.append('Go!')
if ans[-1] != 'Go!':
    ans.append('Go!')
print(*ans)
