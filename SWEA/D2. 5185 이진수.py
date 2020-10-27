HEX = '0123456789ABCDEF'
BIN = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
 
 
T = int(input())
for tc in range(1, T + 1):
    N, st = input().split()
    N = int(N)
 
    print(f'#{tc}', end=' ')
    for ch in st:
        for i in range(16):
            if HEX[i] == ch:
                print(BIN[i], end='')
    print()