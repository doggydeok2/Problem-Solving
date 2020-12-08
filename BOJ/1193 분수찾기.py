N = int(input())
for i in range(5000):
    if i * (i + 1) // 2 >= N:
        tot = i + 1
        th = N - i * (i - 1) // 2
        print(f'{th}/{tot - th}') if tot % 2 else print(f'{tot - th}/{th}')
        break
