from collections import defaultdict

extensions = defaultdict(int)
for _ in range(int(input())):
    extension = input().split('.')[-1]
    extensions[extension] += 1
for key, val in sorted(extensions.items()):
    print(key, val)
