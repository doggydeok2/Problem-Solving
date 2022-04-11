import itertools


while True:
    inp = list(input().split())
    if len(inp) == 1:
        break
    for v in itertools.combinations(inp[1:], 6):
        print(*v)
    print()
