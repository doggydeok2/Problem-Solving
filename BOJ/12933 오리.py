def check_one(_idx):
    ptr = 0
    for i in range(_idx, len(string)):
        if string[i] == target[ptr] and not visited[i]:
            visited[i] = True
            ptr = (ptr + 1) % 5
    return 1 if ptr == 0 else -1023


target = 'quack'
string = input()
visited = [False] * len(string)
cnt = 0

for idx in range(len(string)):
    if string[idx] == 'q' and not visited[idx]:
        cnt += check_one(idx)
print(cnt if cnt > 0 and visited.count(False) == 0 else -1)
