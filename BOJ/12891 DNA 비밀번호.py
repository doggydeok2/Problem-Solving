S, P = map(int, input().split())
string = input()
needs = list(map(int, input().split()))
idx_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
cnt = [0] * 4
satisfied, ans = needs.count(0), 0
for i, ch in enumerate(string):
    ch_idx, prev_ch_idx = idx_dict[ch], idx_dict[string[i - P]]
    cnt[ch_idx] += 1
    satisfied += cnt[ch_idx] == needs[ch_idx]
    if i >= P:
        satisfied -= cnt[prev_ch_idx] == needs[prev_ch_idx]
        cnt[idx_dict[string[i - P]]] -= 1
    if i + 1 >= P:
        ans += satisfied == 4
print(ans)
