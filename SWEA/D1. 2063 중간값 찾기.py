cnt = input()
inputs = list(map(int, input().split()))
inputs.sort()
print(inputs[len(inputs) // 2])
