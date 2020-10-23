digits = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    decode = [0] * 8
    ans = 0
    for _ in range(N):
        line = input()
        ptr, idx = 0, 0
        for i in range(M - 1, -1, -1):
            if line[i] == '1':
                idx = i
                break
        if idx >= 55:
            ptr = 0
            for i in range(idx - 55, idx + 1, 7):
                digit = line[i:i+7]
                for k in range(10):
                    if digit == digits[k]:
                        decode[ptr] = k
                        ptr += 1

    if not (3 * (decode[0] + decode[2] + decode[4] + decode[6]) + decode[1] + decode[3] + decode[5] + decode[7]) % 10:
        ans = sum(decode)

    print(f'#{tc} {ans}')