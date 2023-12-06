import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def can_move(rr, cc, day):
    for i in range(4):
        dx, dy = dt[i]
        nx, ny = rr + dx, cc + dy
        if not A[nx][ny]:
            if not V[nx][ny] or V[nx][ny] <= day:
                return True
    return False


def solve(r, c, d):
    result = 0
    for day in range(1, M + 1):
        if not A[r][c] and not V[r][c]:
            if can_move(r, c, day):
                S[r][c] += 1
                V[r][c] = day + S[r][c] + 4
        elif V[r][c] and V[r][c] <= day:
            V[r][c] = 0
            result += 1

        for i in range(4):
            dx, dy = dt[(d + 1 - i) % 4]
            nx, ny = r + dx, c + dy
            if not A[nx][ny]:
                if not V[nx][ny] or V[nx][ny] <= day:
                    r, c, d = nx, ny, (d + 1 - i) % 4
                    break
    return result


T = int(input())
dt = ((0, 1), (1, 0), (0, -1), (-1, 0))
dts = ['>', 'v', '<', '^']
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if A[r][c]: continue
            for d in range(4):
                V = [[0] * N for _ in range(N)]
                S = [[0] * N for _ in range(N)]
                answer = max(answer, solve(r, c, d))
    print(f'#{tc} {answer}')