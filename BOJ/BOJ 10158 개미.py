W, H = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
tw, th = t % (2 * W), t % (2 * H)

if p + tw <= W:
    p = p + tw
elif W < p + tw <= 2 * W:
    p = W - (tw - (W - p))
else:
    p = tw - (2 * W - p)
if q + th <= H:
    q = q + th
elif H < q + th <= 2 * H:
    q = H - (th - (H - q))
else:
    q = th - (2 * H - q)

print(p, q)