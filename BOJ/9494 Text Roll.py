n = int(input())
while n:
    ans = 0
    for _ in range(n):
        x = input() + ' '
        for i in range(ans, len(x)):
            if x[i] == ' ':
                ans = i
                break
    print(ans + 1)
    n = int(input())
