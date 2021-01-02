sen = input()
for i in range(len(sen) // 10):
    print(sen[(10*i):(10*i)+10])
print(sen[len(sen)//10*10:])