import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
checkArr = [-1] * N

stack = [0] * N
i, ptr = 1, 0

while i < N:
    while seq[stack[ptr]] < seq[i] and ptr >= 0:
        checkArr[stack[ptr]] = seq[i]
        ptr -= 1
    ptr += 1
    stack[ptr] = i
    i += 1
print(*checkArr)
