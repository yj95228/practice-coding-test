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