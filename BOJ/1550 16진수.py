hex_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15
}
num = input()
ans = 0
for idx, val in enumerate(num):
    ans += hex_dict[val] * (16 ** (len(num) - idx - 1))
print(ans)
