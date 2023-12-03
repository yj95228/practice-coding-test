import sys
input = sys.stdin.readline

def make_snail():
    sr, sc, d = N//2, N//2, -1
    dt = ((-1,0),(0,1),(1,0),(0,-1))
    V = [[0]*N for _ in range(N)]
    V[sr][sc] = 1
    snail = [(sr, sc)]
    for _ in range(N*N-1):
        dx, dy = dt[(d+1)%4]
        nx, ny = sr+dx, sc+dy
        if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
            V[nx][ny] = 1
            sr, sc, d = nx, ny, (d+1)%4
            snail.append((nx, ny))
        else:
            dx, dy = dt[d]
            nx, ny = sr+dx, sc+dy
            V[nx][ny] = 1
            snail.append((nx, ny))
            sr, sc = nx, ny
    return snail

N, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
snail = make_snail()
answer = 987654321
for rr, cc in snail:
    B = [row[:] for row in A]
    for dx, dy in ((0,0),(1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = rr+dx, cc+dy
        if 0 <= nx < N and 0 <= ny < N:
            B[nx][ny] *= 2
    cnt, sm = 0, 0
    for r, c in snail[1:]:
        cnt += 1
        if cnt > answer: break
        sm += B[r][c]
        if sm >= H:
            answer = min(answer, cnt)
            break
print('HUNGRY' if answer == 987654321 else answer)