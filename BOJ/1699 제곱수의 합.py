# 33560 KB / 2064 ms
N = int(input())
i = 2
available = [1]

while i ** 2 <= N:
    available.append(i ** 2)
    i += 1

checked = [0] + available[:]
cnt_arr = [0] * (N + 1)

for n in checked:
    for square in available:
        val = n + square
        if val <= N and not cnt_arr[val]:
            checked.append(val)
            cnt_arr[val] = cnt_arr[n] + 1
            if val == N:
                print(cnt_arr[val])
                break
    if cnt_arr[N]:
        break


# 다른 사람의 코드 참고. 35860 KB / 88 ms 
# N = int(input())
# i = 2
# once = {i ** 2 for i in range(1, int(N ** 0.5) + 1)}
# if N in once:
#     print(1)
# else:
#     twice = {i + j for i in once for j in once}
#     if N in twice:
#         print(2)
#     else:
#         three_times_reverse = {N - i for i in twice}
#         print(3 if once & three_times_reverse else 4)
