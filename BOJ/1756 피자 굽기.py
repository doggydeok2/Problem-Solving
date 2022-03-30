D, N = map(int, input().split())
ovens = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

for i in range(1, D):
    ovens[i] = min(ovens[i], ovens[i - 1])

ptr, top = D, 0
for pizza in pizzas:
    ptr -= 1
    while ptr >= 0 and ovens[ptr] < pizza:
        ptr -= 1
    top = ptr + 1
    if ptr < 0:
        break
print(top)
