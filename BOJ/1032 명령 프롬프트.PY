N = int(input())
pattern = list(input())
for _ in range(N - 1):
    file = input()
    for idx, ch in enumerate(file):
        if pattern[idx] == ch:
            continue
        pattern[idx] = '?'
print(''.join(pattern))
