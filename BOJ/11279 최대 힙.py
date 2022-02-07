import sys
rl = sys.stdin.readline


def heappop():
    if ptr == 1:
        return 0
    elif ptr == 2:
        return arr[1]
    else:
        val = arr[1]
        idx, end = 1, ptr - 2
        arr[1] = arr[ptr - 1]

        while idx * 2 <= end:
            biggest = idx * 2 + 1 if idx * 2 + 1 <= end and arr[idx * 2] < arr[idx * 2 + 1] else idx * 2
            if arr[idx] < arr[biggest]:
                arr[idx], arr[biggest] = arr[biggest], arr[idx]
                idx = biggest
            else:
                break
        return val


def heappush(_idx, _n):
    arr[_idx] = _n
    while _idx > 1 and arr[_idx] > arr[_idx // 2]:
        arr[_idx], arr[_idx // 2] = arr[_idx // 2], arr[_idx]
        _idx //= 2


N = int(rl())
arr = [0] * (N + 1)
ptr = 1

for i in range(N):
    n = int(rl())
    if n == 0:
        print(heappop())
        if ptr > 1:
            ptr -= 1
    else:
        heappush(ptr, n)
        ptr += 1
