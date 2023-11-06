N, M = map(int, input().split())
A = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
V = [[0]*(M+2) for _ in range(N+2)]
cnt, wall, fire = 0, [], []
for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r][c] == 0:
            cnt += 1
            wall.append((r, c))
        elif A[r][c] == 2:
            fire.append((r, c))
            V[r][c] = 1
            A[r][c] = 0

length = len(wall)
answer = 0
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            (r1, c1), (r2, c2), (r3, c3) = wall[i], wall[j], wall[k]
            A[r1][c1] = A[r2][c2] = A[r3][c3] = 1
            queue = fire[:]
            visited = [row[:] for row in V]
            result = cnt-3
            while queue:
                next_q = []
                for r, c in queue:
                    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        nx, ny = r+dx, c+dy
                        if not visited[nx][ny] and not A[nx][ny]:
                            visited[nx][ny] = 1
                            result -= 1
                            next_q.append((nx, ny))
                queue = next_q
            A[r1][c1] = A[r2][c2] = A[r3][c3] = 0
            answer = max(answer, result)
print(answer)