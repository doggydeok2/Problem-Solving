data = input()
cnt = 0
for i in range(1, len(data)):
    if data[i] != data[i - 1]: cnt += 1
print(cnt // 2 + 1 if cnt % 2 else cnt // 2)