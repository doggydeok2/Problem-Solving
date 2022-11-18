alphabets = 'abcdefghijklmnopqrstuvwxyz______ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for ch in input():
    print(alphabets[ord(ch) - 65], end='')
