alphabet = 'abcdefghijklmnopqrstuvwxyz'


def checking_ana():
    for c in range(26):
        if cntTgArr[c] != cntDataArr[c]:
            return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    tg, data = input().split()
    cntTgArr, cntDataArr = [0] * 26, [0] * 26
    lenTg, lenData = len(tg), len(data)
    cnt = 0

    for ch in tg:
        for i in range(26):
            if alphabet[i] == ch:
                cntTgArr[i] += 1

    for x in range(lenData):
        for i in range(26):
            if alphabet[i] == data[x]:
                cntDataArr[i] += 1
            if x >= lenTg and alphabet[i] == data[x - lenTg]:
                cntDataArr[i] -= 1
        if x >= lenTg - 1 and checking_ana():
            cnt += 1

    print(f'#{tc} {cnt}')