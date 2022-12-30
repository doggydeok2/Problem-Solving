import collections


N = int(input())
cnt = collections.Counter([input()[0] for _ in range(N)])
print(''.join(sorted([k if cnt[k] >= 5 else '' for k in cnt.keys()])) or 'PREDAJA')
