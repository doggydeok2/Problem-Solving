string = input()
partitions = [input() for _ in range(int(input()))]
DP = [0] * len(string)
able_check_idx = [0]
for i in range(len(string)):
    for idx in able_check_idx:
        if string[idx:i + 1] in partitions:
            DP[i] = 1
            able_check_idx.append(i + 1)
            break
print(DP[-1])
