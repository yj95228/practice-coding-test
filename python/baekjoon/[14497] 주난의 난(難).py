import sys
input = sys.stdin.readline

def solve():
    def dfs(r, c):
        if A[r][c] == '1':
            next_q.append((r, c))
            return
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < M and not V[nx][ny]:
                V[nx][ny] = 1
                dfs(nx, ny)

    V = [[0] * M for _ in range(N)]
    V[sr][sc] = 1
    queue = [(sr, sc)]
    jump = 0

    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec):
                return jump
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny]:
                    V[nx][ny] = 1
                    dfs(nx, ny)
        jump += 1
        queue = next_q


N, M = map(int, input().split())
sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
A = [list(input().rstrip()) for _ in range(N)]
A[sr][sc] = '0'
A[er][ec] = '1'
print(solve())