import sys
input = sys.stdin.readline

def solve():
    sr, sc, sd = 0, 0, 0
    for x in arr:
        if x == 'F':
            dx, dy = dt[sd]
            nx, ny = sr + dx, sc + dy
            if 0 <= nx < N and 0 <= ny < N:
                sr, sc = nx, ny
                if A[sr][sc] == 'S':
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                        nx, ny = sr + dx, sc + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            B[nx][ny] = 1
        elif x == 'L':
            sd = (sd + 1) % 4
        elif x == 'R':
            sd = (sd - 1) % 4

        for i, (r, c, d) in enumerate(zombie):
            if (r, c) == (sr, sc) and not (B[r][c] or A[r][c] == 'S'): return 'Aaaaaah!'
            dx, dy = dt[d]
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < N:
                zombie[i][0], zombie[i][1] = nx, ny
            else:
                zombie[i][-1] = (d + 2) % 4

            r, c, d = zombie[i]
            if B[r][c] or A[r][c] == 'S':
                continue
            elif (r, c) == (sr, sc):
                return 'Aaaaaah!'
    return 'Phew...'

N = int(input())
arr = list(input().rstrip())
A = [list(input().rstrip()) for _ in range(N)]
B = [[0]*N for _ in range(N)]
dt = ((1,0),(0,1),(-1,0),(0,-1))
zombie = []
for r in range(N):
    for c in range(N):
        if A[r][c] == 'Z':
            zombie.append([r, c, 0])
            A[r][c] = 'O'
print(solve())