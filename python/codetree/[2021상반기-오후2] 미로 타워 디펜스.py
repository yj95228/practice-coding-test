import sys
input = sys.stdin.readline

def make_snail():
    snail = []
    snail_dt = ((0,-1),(1,0),(0,1),(-1,0))
    V = [[0]*N for _ in range(N)]
    sr, sc, sd = N//2, N//2, -1
    V[sr][sc] = 1
    for _ in range(N*N-1):
        dx, dy = snail_dt[(sd+1)%4]
        nx, ny = sr+dx, sc+dy
        if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
            V[nx][ny] = 1
            snail.append((nx, ny))
            sr, sc, sd = nx, ny, (sd+1)%4
        else:
            dx, dy = snail_dt[sd]
            nx, ny = sr+dx, sc+dy
            V[nx][ny] = 1
            snail.append((nx, ny))
            sr, sc = nx, ny
    return snail

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dt = ((0,1),(1,0),(0,-1),(-1,0))
snail = make_snail()

answer = [0]*4
for _ in range(M):
    d, p = map(int, input().split())
    dx, dy = dt[d]
    for i in range(1, p+1):
        nx, ny = N//2+i*dx, N//2+i*dy
        if 0 <= nx < N and 0 <= ny < N:
            if A[nx][ny]:
                answer[A[nx][ny]] += 1
                A[nx][ny] = 0
        else: break

    queue = []
    for r, c in snail:
        if A[r][c]:
            queue.append(A[r][c])

    while queue:
        flag = False
        next_q, temp_q = [], []
        for x in queue:
            if not temp_q:
                temp_q.append(x)
            elif temp_q[-1] != x:
                if len(temp_q) >= 4:
                    answer[temp_q[-1]] += len(temp_q)
                    flag = True
                else:
                    next_q.extend(temp_q)
                temp_q = [x]
            else:
                temp_q.append(x)
        if len(temp_q) >= 4:
            answer[temp_q[-1]] += len(temp_q)
            flag = True
        else:
            next_q.extend(temp_q)
        if flag: queue = next_q
        else: break

    nqueue = []
    for x in queue:
        if nqueue and nqueue[-1] == x:
            nqueue[-2] += 1
        else:
            nqueue.extend([1, x])

    A = [[0]*N for _ in range(N)]
    for i, (r, c) in enumerate(snail):
        if i < len(nqueue):
            A[r][c] = nqueue[i]
        else: break

print(sum([i*x for i, x in enumerate(answer)]))