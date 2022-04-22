import collections


N = int(input())
cnt = collections.Counter([int(input()) for _ in range(N)])
ans = cnt_ans = 0
for key in cnt:
    if cnt_ans < cnt[key] or cnt_ans == cnt[key] and ans > key:
        ans = key
        cnt_ans = cnt[key]
print(ans)
