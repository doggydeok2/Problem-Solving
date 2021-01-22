exp = input() + '+'
exL = len(exp)

s = num1 = num2 = i = minusSign = 0
while i < exL:
    if exp[i] == '+' or exp[i] == '-':
        num2 = int(exp[s:i])
        num1 += num2 if not minusSign else -num2
        if not minusSign and exp[i] == '-':
            minusSign = 1
        s = i + 1
    i += 1
print(num1)
