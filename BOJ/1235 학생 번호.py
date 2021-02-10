N = int(input())
numbers = [input() for _ in range(N)]
l = len(numbers[0])

for i in range(1, l + 1):
    numParts = set([numbers[x][l - i:] for x in range(N)])
    if len(numParts) == N:
        print(i)
        break
