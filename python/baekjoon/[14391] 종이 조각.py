import sys

input = sys.stdin.readline


def init():
    for r in range(N):
        for c in range(M):
            if not V[r][c]:
                return r, c
    return None, None


def recur(result):
    global answer
    sr, sc = init()
    if sr is None:
        answer = max(answer, result)
        return

    num, visited = [], []
    for k in range(N):
        if sr + k >= N or V[sr + k][sc]: break
        V[sr + k][sc] = 1
        visited.append((sr + k, sc))
        num.append(A[sr + k][sc])
        recur(result + int(''.join(num)))
    for r, c in visited:
        V[r][c] = 0

    num, visited = [], []
    for k in range(M):
        if sc + k >= M or V[sr][sc + k]: break
        V[sr][sc + k] = 1
        visited.append((sr, sc + k))
        num.append(A[sr][sc + k])
        recur(result + int(''.join(num)))
    for r, c in visited:
        V[r][c] = 0


N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0] * M for _ in range(N)]
answer = 0
recur(0)
print(answer)