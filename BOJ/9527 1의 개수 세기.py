def cal(_n):
    cnt = 0
    for i in range(1, 56):
        prev, curr = (2 ** (i - 1)), 2 ** i
        ones = prev * (_n // curr) + (_n % curr - prev + 1 if _n % curr >= prev else 0)
        if ones == 0:
            return cnt
        cnt += ones


A, B = map(int, input().split())
print(cal(B) - cal(A - 1))
