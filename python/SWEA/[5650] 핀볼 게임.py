# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo
def play(dd, rr, cc):
    stack = [(dd, rr, cc)]
    score = 0
    while stack:
        d, r, c = stack.pop()
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if matrix[nx][ny] == -1:
            return score
        elif matrix[nx][ny] <= 5:
            nd = dts[matrix[nx][ny]][d]
            if (nx, ny) == (rr, cc): return score
            if matrix[nx][ny]: score += 1
            stack.append((nd, nx, ny))
        else:
            nnx, nny = wormhole[(nx, ny)]
            stack.append((d, nnx, nny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[5]*(N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5]*(N+2)]
    dt = ((1,0),(0,1),(-1,0),(0,-1))
    dts = [(0,1,2,3),(1,3,0,2),(2,3,1,0),(2,0,3,1),(3,2,0,1),(2,3,0,1)]
    answer, can, worm, wormhole = 0, [], [[] for _ in range(5)], dict()
    for r in range(1,N+1):
        for c in range(1,N+1):
            if not matrix[r][c]:
                can.append((r,c))
            elif matrix[r][c] >= 6:
                worm[matrix[r][c]-6].append((r,c))
    for w in worm:
        if not w: break
        (r1, c1), (r2, c2) = w
        wormhole[(r1, c1)] = (r2, c2)
        wormhole[(r2, c2)] = (r1, c1)
    for r, c in can:
        for d in range(4):
            answer = max(answer, play(d, r, c))
    print(f'#{tc} {answer}')

# 2차 풀이
def play(sr, sc, sd):
    queue = [(sr, sc, sd)]
    cnt = 0
    while queue:
        next_q = []
        for r, c, d in queue:
            dx, dy = dt[d]
            nx, ny = r + dx, c + dy
            if A[nx][ny] == -1 or (nx, ny) == (sr, sc): return cnt
            if A[nx][ny] <= 5:
                nd = rotate[A[nx][ny]][d]
                next_q.append((nx, ny, nd))
                if A[nx][ny]: cnt += 1
            else:
                nnx, nny = obj[(nx, ny)]
                next_q.append((nnx, nny, d))
        queue = next_q


T = int(input())
dt = ((1, 0), (0, 1), (-1, 0), (0, -1))
rotate = (((0,1,2,3)),((1,3,0,2)),((2,3,1,0)),((2,0,3,1)),((3,2,0,1)),((2,3,0,1)))
for tc in range(1, T + 1):
    N = int(input())
    A = [[5] * (N + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N + 2)]
    worm = [[] for _ in range(11)]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if 6 <= A[r][c]:
                worm[A[r][c]].extend((r, c))
    obj = dict()
    for i in range(6, 11):
        if worm[i]:
            r1, c1, r2, c2 = worm[i]
            obj[(r1, c1)] = (r2, c2)
            obj[(r2, c2)] = (r1, c1)
    answer = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if A[r][c]: continue
            for d in range(4):
                answer = max(answer, play(r, c, d))
    print(f'#{tc} {answer}')