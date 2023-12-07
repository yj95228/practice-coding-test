import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(r, c):
    V = [[0] * M for _ in range(N)]
    V[r][c] = 1
    queue = [(r, c)]
    turn = 0
    while queue:
        next_q = []
        for x, y in queue:
            if A[x][y]: return turn
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        # print(next_q)
        queue = next_q
        turn += 1

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
blank = []
for r in range(N):
    for c in range(M):
        if not A[r][c]:
            blank.append((r, c))
answer = 0
for r, c in blank:
    answer = max(answer, bfs(r, c))
print(answer)