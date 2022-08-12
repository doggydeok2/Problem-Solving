def get_apple_num(N):
    if N == 1:
        return 1
    remainders = [-1] * (N + 1)
    sub_nums = [0, 1]
    remainders[0], remainders[1], remainders[N] = 0, 1, 0

    powers = 1
    while True:
        n = 1 * (10 ** powers)
        gap = N - n % N
        if remainders[gap] != -1:
            return n + remainders[gap]

        len_sub = len(sub_nums)
        for i in range(len_sub):
            assembled = n + sub_nums[i]
            n_remainder = assembled % N
            if remainders[n_remainder] != -1:
                continue
            remainders[n_remainder] = assembled
            sub_nums.append(assembled)
        powers += 1


for _ in range(int(input())):
    print(get_apple_num(int(input())))
