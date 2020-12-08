N = int(input())
remainder = [3, 4, 5, 4, 5, 4, 5, 6, 5, 6, 5, 6, 7, 6, 7]
if N == 4 or N == 7: print(-1)
# elif N < 15: print(remainder[N % 15] - 3)
else: print(3 * ((N - 15) // 15) + remainder[N % 15])