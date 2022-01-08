N = int(input())
solutions = list(map(int, input().split()))
min_sum = int(2e10)
l = min_l = 0
r = min_r = N - 1

while l < r:
    temp_sum = abs(solutions[l] + solutions[r])
    if min_sum > temp_sum:
        min_sum = temp_sum
        min_l = l
        min_r = r

    if solutions[l] + solutions[r] > 0:
        r -= 1
    else:
        l += 1

print(solutions[min_l], solutions[min_r])
