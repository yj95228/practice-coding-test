import sys
input = sys.stdin.readline

V, E = map(int, input().split())
D = [[987654321]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    D[a][b] = c

for x in range(1, V+1):
    D[x][x] = 0

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

answer = 987654321
for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j: continue
        answer = min(answer, D[i][j]+D[j][i])
print(-1 if answer == 987654321 else answer)