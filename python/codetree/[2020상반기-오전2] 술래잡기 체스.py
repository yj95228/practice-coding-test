def find(A, idx):
    for r in range(4):
        for c in range(4):
            if A[r][c][0] == idx:
                return r, c

def fish_move(er, ec, A):
    for idx in range(16):
        if dead[idx]: continue
        r, c = find(A, idx+1)
        tmp = A[r][c]
        if tmp[0] is None: continue
        num, d = tmp
        for nd in range(8):
            dx, dy = dt[(d + nd) % 8]
            nx, ny = r + dx, c + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (er, ec):
                A[r][c], A[nx][ny] = A[nx][ny], A[r][c]
                A[nx][ny][1] = (d + nd) % 8
                break
    return A

def recur(er, ec, ed, score, A):
    global answer
    answer = max(answer, score)

    B = fish_move(er, ec, [[x[:] for x in row] for row in A])

    dx, dy = dt[ed]
    for d in range(1, 4):
        nx, ny = er + d * dx, ec + d * dy
        if 0 <= nx < 4 and 0 <= ny < 4 and B[nx][ny]:
            tmp = B[nx][ny]
            if tmp[0] is None: continue
            num, nd = B[nx][ny]
            B[nx][ny] = [None]
            dead[num-1] = 1
            recur(er + d * dx, ec + d * dy, nd, score+num, [[x[:] for x in row] for row in B])
            B[nx][ny] = [num, nd]
            dead[num-1] = 0


A = []  # [물고기 번호, 방향]
for r in range(4):
    arr = list(map(int, input().split()))
    temp = []
    for c in range(4):
        temp.append([arr[2*c], arr[2*c+1]-1])
    A.append(temp)

dead = [0]*16   # 죽은 물고기
dt = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)) # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dts = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
answer = 0

# (0,0)부터 먹기
num, d = A[0][0]
A[0][0] = [None]
er, ec, ed = 0, 0, d
answer += num
dead[num-1] = 1

recur(er, ec, ed, num, A)
print(answer)

# 2차 풀이
import sys
input = sys.stdin.readline

def solve(sr, sc, sd, A, fish, dead, score):
    global answer
    answer = max(answer, score)
    for idx, (r, c, d) in enumerate(fish[1:], start=1):
        if dead[idx]: continue
        for i in range(8):
            dx, dy = dt[(d + i) % 8]
            nx, ny = r + dx, c + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sr, sc):
                fish[idx] = [nx, ny, (d + i) % 8]
                if A[nx][ny]:
                    nidx = A[nx][ny]
                    fish[nidx][0], fish[nidx][1] = r, c
                A[r][c], A[nx][ny] = A[nx][ny], A[r][c]
                break

    dx, dy = dt[sd]
    for i in range(1, 4):
        nx, ny = sr + i*dx, sc + i*dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if A[nx][ny]:
                nidx = A[nx][ny]
                dead[nidx] = 1
                score += nidx
                A[nx][ny] = 0
                solve(nx, ny, fish[nidx][-1], [row[:] for row in A], [row[:] for row in fish], dead[:], score)
                A[nx][ny] = nidx
                score -= nidx
                dead[nidx] = 0
        else: break

A, fish = [], [[0]*3 for _ in range(17)]
dt = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))
dts = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
for r in range(4):
    arr = list(map(int, input().split()))
    row = []
    for c in range(4):
        idx, d = arr[2*c], arr[2*c+1]-1
        row.append(idx)
        fish[idx] = [r, c, d]
    A.append(row)

dead = [0]*17
idx = A[0][0]
answer = idx
dead[idx] = 1
A[0][0] = 0
solve(0, 0, fish[idx][-1], [row[:] for row in A], [row[:] for row in fish], dead[:], answer)
print(answer)