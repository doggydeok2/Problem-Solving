def isInfEqual(_s1, _s2):
    for i in range(len(_s2) * len(_s1)):
        if _s1[i % len(_s1)] != _s2[i % len(_s2)]:
            return 0
    return 1


strings = sorted([input() for _ in range(2)], key=lambda x: len(x))
print(isInfEqual(strings[0], strings[1]))
