input()
times = sorted(list(map(int, input().split())), reverse=True)
print(max([idx + time + 2 for idx, time in enumerate(times)]))
