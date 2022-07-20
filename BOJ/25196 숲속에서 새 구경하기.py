def ans():
    birds = sorted([list(map(int, input().split())) for _ in range(3)], key=lambda x: (x[2] - x[1], -x[0]))
    Av, As, Ae = birds[0]
    Bv, Bs, Be = birds[1]
    Cv, Cs, Ce = birds[2]

    if Av == Bv and (Ae < Bs or Be < As) or \
        Bv == Cv and (Be < Cs or Ce < Bs) or \
        Cv == Av and (Ce < As or Ae < Cs):
        return -1

    for m in range(0, Av * Bv * Cv, Av):
        for t in range(m + As, m + Ae + 1):
            if Cs <= t % Cv <= Ce and Bs <= t % Bv <= Be:
                return t
    return -1


print(ans())
