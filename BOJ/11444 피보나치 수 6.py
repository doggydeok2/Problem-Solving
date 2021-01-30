# A + B == N 인 N에 대해서
# fibo(N) = fibo(B + 1) * fibo(A) + fibo(B) * fibo(A -1)


def find_idx(x):
    for i in range(cnt):
        if idx[i] == x:
            return i
    return 0


def cal_fibo(n):
    global cnt
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        ptr = find_idx(n)
        if ptr:
            return val[ptr]
        else:
            half = cal_fibo(n // 2)
            temp = (cal_fibo(n // 2 + 1) ** 2 + half ** 2) % p if n % 2 else (cal_fibo(n // 2 + 1) * half + half * cal_fibo(n // 2 - 1)) % p
            idx.append(n)
            val.append(temp)
            cnt += 1
            return temp


idx, val = [], []
cnt, p = 0, 1000000007
print(cal_fibo(int(input())))
