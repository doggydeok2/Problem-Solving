T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    if B > A:
        A, B = B, A

    oA, oB, c = A, B, A % B
    while c:
        B, c = c, B % c
    print(oA * oB // B)
