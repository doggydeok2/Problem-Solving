import collections


def check_visit(_a, _b, _c):
    if not visited[_a][_b][_c]:
        visited[_a][_b][_c] = True
        q.append((_a, _b, _c))
        if _a == 0:
            ans[_c] = True


A, B, C = map(int, input().split())
visited = [[[False] * (C + 1) for _ in range(B + 1)] for __ in range(A + 1)]
ans = [False] * 201
visited[0][0][C] = ans[C] = True
q = collections.deque([(0, 0, C)])
while q:
    ta, tb, tc = q.popleft()
    if ta != A:
        tb and check_visit(min(ta + tb, A), max(0, tb + ta - A), tc)
        tc and check_visit(min(ta + tc, A), tb, max(0, tc + ta - A))
    if tb != B:
        ta and check_visit(max(0, ta + tb - B), min(ta + tb, B), tc)
        tc and check_visit(ta, min(tb + tc, B), max(0, tc + tb - B))
    if tc != C:
        ta and check_visit(max(0, ta + tc - C), tb, min(ta + tc, C))
        tb and check_visit(ta, max(0, tb + tc - C), min(tb + tc, C))
for i in range(201):
    if ans[i]:
        print(i, end=' ')
