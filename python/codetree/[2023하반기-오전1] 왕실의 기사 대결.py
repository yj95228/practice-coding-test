# https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20
from sys import stdin
from collections import deque
input = stdin.readline

def move(idx, d, start):
    r, c, h, w, k, s = robot[idx]
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    for rr in range(nx, nx+h):
        for cc in range(ny, ny+w):
            narr[rr][cc] = idx
            if A[rr][cc] == 1 and idx != start:
                s += 1
    if k <= s:
        dead[idx] = 1
        for rr in range(nx, nx+h):
            for cc in range(ny, ny+w):
                narr[rr][cc] = 0
    robot[idx] = [nx, ny, h, w, k, s]

def stay(idx):
    r, c, h, w, k, s = robot[idx]
    for rr in range(r, r+h):
        for cc in range(c, c+w):
            narr[rr][cc] = idx

def solve(idx, d):
    def can_move(idx, d):
        dx, dy = dt[d]
        queue = deque()
        r, c, h, w, _, _ = robot[idx]
        nx, ny = r+dx, c+dy
        for rr in range(nx, nx+h):
            for cc in range(ny, ny+w):
                queue.append((idx, rr, cc))
        while queue:
            idx, r, c = queue.popleft()
            if A[r][c] == 2: return False
            elif matrix[r][c] and matrix[r][c] != idx:
                idxs[matrix[r][c]] = 1
                rr, cc, h, w, _, _ = robot[matrix[r][c]]
                nx, ny = rr+dx, cc+dy
                for rrr in range(nx, nx+h):
                    for ccc in range(ny, ny+w):
                        queue.append((matrix[r][c], rrr, ccc))
        return True

    idxs = [0]*(N+1)
    idxs[idx] = 1
    if dead[idx] or can_move(idx, d):
        for i in range(1, N+1):
            if dead[i]: continue
            elif idxs[i]: move(i, d, idx)
            else: stay(i)
    else:
        for i in range(1, N+1):
            if dead[i]: continue
            stay(i)

L, N, Q = map(int, input().split())
dt = ((-1,0),(0,1),(1,0),(0,-1))
A = [[2]*(L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
matrix = [[0]*(L+2) for _ in range(L+2)]
robot = [[]]
dead = [0]*(N+1)
for idx in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    robot.append([r, c, h, w, k, 0])
    for rr in range(r, r+h):
        for cc in range(c, c+w):
            matrix[rr][cc] = idx

for _ in range(Q):
    narr = [[0]*(L+2) for _ in range(L+2)]
    i, d = map(int, input().split())
    solve(i, d)
    matrix = narr

answer = 0
for i in range(1, N+1):
    if dead[i]: continue
    answer += robot[i][-1]
print(answer)