N = int(input())
chicken = others = 0
foods = input()
for food in foods:
    if food == 'C':
        chicken += 1
    else:
        others += 1
div, mod = divmod(chicken, others + 1)
print(div + (mod != 0))