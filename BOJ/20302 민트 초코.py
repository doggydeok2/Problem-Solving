import collections

N = int(input())
string = list(input().split(" "))
is_multiple = True
cnt_dict = collections.defaultdict(int)

for ch in string:
    if ch == "*": is_multiple = True
    elif ch == "/": is_multiple = False
    else:
        cnt_dict[ch] += 1 if is_multiple else -1

numerator = denominator = 1
for (key, val) in cnt_dict.items():
    if val > 0:
        numerator *= int(key) ** val
    elif val < 0:
        denominator *= int(key) ** (-val)

print("mint chocolate" if numerator % denominator == 0 else "toothpaste")
