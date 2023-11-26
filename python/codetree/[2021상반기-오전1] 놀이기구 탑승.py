import sys
input = sys.stdin.readline

N = int(input())
A = [[0]*N for _ in range(N)]
friends = [[] for _ in range(N*N+1)]
for _ in range(N*N):
    n0, n1, n2, n3, n4 = map(int, input().split())
    friends[n0] = [n1, n2, n3, n4]
    likes, emptys = 0, 0
    best = [N, N]
    for r in range(N):
        for c in range(N):
            if A[r][c]: continue
            like, empty = 0, 0
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not A[nx][ny]: empty += 1
                    elif A[nx][ny] in [n1, n2, n3, n4]: like += 1
            if likes < like:
                likes, emptys = like, empty
                best = [r, c]
            elif likes == like:
                if emptys < empty:
                    emptys = empty
                    best = [r, c]
                elif emptys == empty:
                    if best[0] > r:
                        best = [r, c]
                    elif best[0] == r:
                        if best[1] > c:
                            best = [r, c]
    x, y = best
    A[x][y] = n0
score = [0, 1, 10, 100, 1000]
answer = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] in friends[A[r][c]]:
                cnt += 1
        answer += score[cnt]
print(answer)