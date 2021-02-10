while True:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        break
    assigned = 'Junior' if int(age) <= 17 and int(weight) < 80 else 'Senior'
    print(name, assigned)