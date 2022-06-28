tg = "UCPC"
idx = 0
for ch in input():
    if ch == tg[idx]:
        idx += 1
        if idx == 4:
            break
print(f"I {'love' if idx == 4 else 'hate'} UCPC")
