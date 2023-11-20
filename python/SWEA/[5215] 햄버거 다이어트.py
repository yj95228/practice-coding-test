# 재귀
def recur(n, value, calory):
    global answer
    if n == N:
        answer = max(answer, value)
        return
    V, W = arr[n]
    if calory+W <= L:
        recur(n+1, value+V, calory+W)
    recur(n+1, value, calory)

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    recur(0, 0, 0)
    print(f'#{tc} {answer}')

# 2차원 dp
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    D = [[0]*(L+1) for _ in range(N+1)]
    for i in range(1, N+1):
        V, W = map(int, input().split())
        for j in range(L+1):
            if W <= j:
                D[i][j] = max(D[i-1][j-W]+V, D[i-1][j])
            else:
                D[i][j] = D[i-1][j]
    print(f'#{tc} {D[N][L]}')

# 1차원 dp
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    D = [0]*(L+1)
    for i in range(1, N+1):
        V, W = map(int, input().split())
        for j in range(L, -1, -1):
            if W <= j:
                D[j] = max(D[j-W]+V, D[j])
    print(f'#{tc} {D[L]}')