def pick_ham():
    p_ptr = h_ptr = cnt = 0
    while True:
        while info[p_ptr] != 'P':
            p_ptr += 1
            if p_ptr == N:
                return cnt
        while info[h_ptr] != 'H':
            h_ptr += 1
            if h_ptr == N:
                return cnt
        if abs(p_ptr - h_ptr) <= K:
            cnt += 1
            p_ptr += 1
            h_ptr += 1
            if h_ptr == N or p_ptr == N:
                return cnt
        else:
            if p_ptr > h_ptr:
                h_ptr += 1
                if h_ptr == N:
                    return cnt
            else:
                p_ptr += 1
                if p_ptr == N:
                    return cnt


N, K = map(int, input().split())
info = input()
print(pick_ham())
