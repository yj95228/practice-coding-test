T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(input().rstrip()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if A[r][c] == '.':
                cnt = 0
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == '*':
                        cnt += 1
                A[r][c] = cnt

    answer = 0
    V = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not A[r][c] and not V[r][c]:
                answer += 1
                V[r][c] = answer
                queue = [(r, c)]
                while queue:
                    next_q = []
                    for rr, cc in queue:
                        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                            nx, ny = rr + dx, cc + dy
                            if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and A[nx][ny] != '*':
                                V[nx][ny] = answer
                                if not A[nx][ny]: next_q.append((nx, ny))
                    queue = next_q
    for r in range(N):
        for c in range(N):
            if not V[r][c] and A[r][c] != '*':
                answer += 1
    print(f'#{tc} {answer}')