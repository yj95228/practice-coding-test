import sys
input = sys.stdin.readline

N, K = map(int, input().split())
D = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        if w <= j:
            D[i][j] = max(D[i-1][j-w]+v, D[i-1][j])
        else:
            D[i][j] = D[i-1][j]
print(D[N][K])