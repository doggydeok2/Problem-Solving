cmd = input()
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'

for i in range(26):
    if i < 10 and number[i] == cmd: print(48 + i)
    elif lower[i] == cmd: print(97 + i)
    elif upper[i] == cmd: print(65 + i)
