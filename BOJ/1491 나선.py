w, h = map(int, input().split())
short = min(w, h)
x = y = 0
cyc = short // 2
if short % 2:
    x = cyc + w - h if w >= h else cyc
    y = cyc if w >= h else cyc + h - w
else:
    x = cyc - 1
    y = cyc
print(x, y)