apartment = [[i for i in range(1, 15)] for j in range(15)]

for i in range(1, 15):
    for j in range(14):
        apartment[i][j] = sum(apartment[i - 1][:j + 1])

for tc in range(int(input())):
    k = int(input())
    n = int(input())
    print(apartment[k][n - 1])
