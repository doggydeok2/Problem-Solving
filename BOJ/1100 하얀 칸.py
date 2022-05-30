print(sum([(i // 8 % 2 + i % 2) % 2 == 0 and val == 'F' for i, val in enumerate(list(''.join([input() for _ in range(8)])))]))
