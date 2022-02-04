import sys
rl = sys.stdin.readline


def heappop():
    leng = len(heap)
    if leng == 1:
        return 0
    elif leng == 2:
        return heap.pop()
    else:
        popped_el = heap[1]
        heap[1] = heap.pop()
        leng -= 1
        ptr = 1

        while ptr * 2 < leng:
            min_child = ptr * 2 + 1 if ptr * 2 + 1 < leng and heap[ptr * 2] > heap[ptr * 2 + 1] else ptr * 2

            if heap[ptr] > heap[min_child]:
                heap[ptr], heap[min_child] = heap[min_child], heap[ptr]
                ptr = min_child
            else:
                break
        return popped_el


def heappush(_n):
    heap.append(_n)
    ptr = len(heap) - 1

    while ptr and heap[ptr // 2] > heap[ptr]:
        heap[ptr // 2], heap[ptr] = heap[ptr], heap[ptr // 2]
        ptr //= 2


N = int(rl())
heap = [0]

for _ in range(N):
    cmd = int(rl())
    if cmd == 0:
        print(heappop())
    else:
        heappush(cmd)
