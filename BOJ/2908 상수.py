data = list(input().split())
A, B = int(data[0][2] + data[0][1] + data[0][0]), int(data[1][2] + data[1][1] + data[1][0])
print(A) if A > B else print(B)