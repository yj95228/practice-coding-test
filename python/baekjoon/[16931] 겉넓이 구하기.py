import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 6*sum([sum(row) for row in A])
for r in range(N):
    for c in range(M):
        answer -= 2*(A[r][c]-1)
        for dx, dy in ((1,0),(0,1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M:
                answer -= 2*min(A[r][c], A[nx][ny])
print(answer)