A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
A_digit = sum([nums[-i] * (A ** (i - 1)) for i in range(1, m + 1)])

B_digits = []
div = B
while A_digit:
    B_digits.append((A_digit % div) // (div // B))
    A_digit -= A_digit % div
    div *= B
print(*B_digits[::-1])
