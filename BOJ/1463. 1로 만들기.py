N = int(input())
v = [0] * (N + 1)
q = [N]

while True:
    num = q.pop(0)
    if num == 1:
        print(v[num])
        break
    n2, n3, n1 = num // 2, num // 3, num - 1
    if not (num % 2 or v[n2]):
        q.append(n2)
        v[n2] = v[num] + 1
    if not (num % 3 or v[n3]):
        q.append(n3)
        v[n3] = v[num] + 1
    if not v[n1]:
        q.append(n1)
        v[n1] = v[num] + 1
