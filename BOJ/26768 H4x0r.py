W = list(input())
change = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
for i, ch in enumerate(W):
    if ch in 'aeios':
        W[i] = change[ch]
print(''.join(W))
