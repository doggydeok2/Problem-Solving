K = int(input())
stack = [0] * K
ptr = 0
for i in range(K):
    N = int(input())
    if N:
        stack[ptr] = N
        ptr += 1
    else:
        ptr -= 1
        stack[ptr] = 0
print(sum(stack))