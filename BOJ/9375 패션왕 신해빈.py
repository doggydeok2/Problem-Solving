def find_type(w, c):
    for x in range(c):
        if w == types[x]:
            cnts[x] += 1
            return 0
    return -1


T = int(input())
for _ in range(T):
    n = int(input())
    types, cnts = [], [0] * n
    cnt = 0

    for i in range(n):
        f, r = input().split()

        if find_type(r, cnt):        
            types.append(r)
            cnts[cnt] += 1
            cnt += 1
    
    total = 1
    for num in cnts:
        total *= num + 1
    print(total - 1)
