import sys
rl = sys.stdin.readline


ORD_A = ord('a')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = rl().rstrip()
cnt_arr = [[0] * (len(S) + 1) for _ in range(26)]
for idx, ch in enumerate(S):
    for th in range(26):
        cnt_arr[th][idx] = cnt_arr[th][idx - 1] + (ch == alphabet[th])

for tc in range(int(rl())):
    ch, s, e = rl().split()
    ord_ch = ord(ch)
    print(cnt_arr[ord_ch - ORD_A][int(e)] - cnt_arr[ord_ch - ORD_A][int(s) - 1])
