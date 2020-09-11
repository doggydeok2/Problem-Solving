def palindrome(words):
    repeat = len(words) // 2
    for _ in range(repeat):
        if words[0] == words[-1]:
            words = words[1:-1]
        else:
            return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    words = input()
    print(f'#{test_case} {palindrome(words)}')
