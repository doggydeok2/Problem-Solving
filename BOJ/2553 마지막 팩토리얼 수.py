ans = 1
for i in range(1, 1 + int(input())):
    ans *= i
    while ans % 10 == 0:
        ans //= 10
    ans %= 1000000
print(ans % 10)
