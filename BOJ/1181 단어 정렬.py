N = int(input())
sens = [0] * N
for i in range(N):
    sens[i] = input()
for sen in sorted(set(sens), key=lambda x: (len(x), x)):
    print(sen)