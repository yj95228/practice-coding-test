import sys

input = sys.stdin.readline


def find(A):
    r1, c1, r2, c2 = None, None, None, None
    for r in range(N):
        for c in range(M):
            if A[r][c] == 'o':
                A[r][c] = '.'
                if r1 is None:
                    r1, c1 = r, c
                else:
                    r2, c2 = r, c
    return r1, c1, r2, c2


def change(A):
    return ''.join(map(lambda x: ''.join(x), A))


def in_range(r, c):
    return 1 if 0 <= r < N and 0 <= c < M else 0


def solve():
    V = set()
    r1, c1, r2, c2 = find(A)
    queue = [(r1, c1, r2, c2)]

    A[r1][c1] = A[r2][c2] = 'o'
    V.add(change(A))
    A[r1][c1] = A[r2][c2] = '.'

    time = 0
    while queue:
        if time > 10: return -1

        next_q = []
        for r1, c1, r2, c2 in queue:
            result = in_range(r1, c1) + in_range(r2, c2)
            if not result: continue
            if result == 1: return time

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx1, ny1 = r1 + dx, c1 + dy
                if in_range(nx1, ny1) and A[nx1][ny1] == '#':
                    nx1, ny1 = r1, c1
                nx2, ny2 = r2 + dx, c2 + dy
                if in_range(nx2, ny2) and A[nx2][ny2] == '#':
                    nx2, ny2 = r2, c2
                if (nx1, ny1) == (nx2, ny2): continue

                if in_range(nx1, ny1): A[nx1][ny1] = 'o'
                if in_range(nx2, ny2): A[nx2][ny2] = 'o'

                v = change(A)
                if v not in V:
                    V.add(v)
                    next_q.append((nx1, ny1, nx2, ny2))

                if in_range(nx1, ny1): A[nx1][ny1] = '.'
                if in_range(nx2, ny2): A[nx2][ny2] = '.'

        queue = next_q
        time += 1

    return -1


N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
print(solve())