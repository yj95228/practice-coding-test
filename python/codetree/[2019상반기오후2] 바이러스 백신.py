def bfs(arr):
    queue = [hospital[x] for x in arr]
    V = [[0]*(N+2) for _ in range(N+2)]
    for r, c in queue:
        V[r][c] = 1
    result = cnt
    time = 0
    while queue:
        if not result: return time
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not V[nx][ny] and A[nx][ny] != 1:
                    if not A[nx][ny]: result -= 1
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
        time += 1
    return 987654321

def recur(n, start, arr):
    if n == M:
        global answer
        result = bfs(arr)
        if result != 987654321:
            answer = min(answer, result)
        return
    for x in range(start, length):
        recur(n+1, x+1, arr+[x])

N, M = map(int, input().split())
A = [[1]*(N+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(N+2)]
cnt, hospital = 0, []
for r in range(1, N+1):
    for c in range(1, N+1):
        if A[r][c] == 0:
            cnt += 1
        elif A[r][c] == 2:
            hospital.append((r, c))
length = len(hospital)
answer = 987654321
recur(0, 0, [])
print(-1 if answer == 987654321 else answer)