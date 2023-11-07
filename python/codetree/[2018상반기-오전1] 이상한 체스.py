def recur(n, result):
    if n == length:
        global answer
        answer = min(result, answer)
        return
    d, r, c = arr[n]
    for dd in dt[d]:
        temp, cnt = [], result
        for dx, dy in dd:
            k = 1
            while True:
                nx, ny = r + k * dx, c + k * dy
                if A[nx][ny] == 6:
                    break
                elif not V[nx][ny] and not A[nx][ny]:
                    temp.append((nx, ny))
                    V[nx][ny] = 1
                    cnt -= 1
                k += 1
        recur(n + 1, cnt)
        for rr, cc in temp:
            V[rr][cc] = 0

N, M = map(int, input().split())
A = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
dt = [
    [],
    [[(1, 0)], [(0, 1)], [(-1, 0)], [(0, -1)]],
    [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)]],
    [[(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]],
    [[(1, 0), (0, 1), (0, -1), (0, -1)]]
]
arr = []
V = [[0] * (M + 2) for _ in range(N + 2)]
empty = 0
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if not A[r][c]:
            empty += 1
        elif 1 <= A[r][c] <= 5:
            arr.append((A[r][c], r, c))

answer = empty
length = len(arr)
recur(0, empty)
print(answer)