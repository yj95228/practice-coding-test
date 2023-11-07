# (y-b+a, -x+a+b)
N = int(input())
A = [[0]*101 for _ in range(101)]
dt = ((0,1),(-1,0),(0,-1),(1,0))

for _ in range(N):
    X, Y, D, G = map(int, input().split())
    stack = [(X, Y)]
    A[X][Y] = 1
    dx, dy = dt[D]
    nx, ny = X+dx, Y+dy
    stack.append((nx, ny))
    A[nx][ny] = 1
    for g in range(G):
        a, b = stack[-1]
        for i in range(len(stack)-2, -1, -1):
            x, y = stack[i]
            stack.append((y-b+a, -x+a+b))
            A[y-b+a][-x+a+b] = 1

answer = 0
for r in range(100):
    for c in range(100):
        if A[r][c] and A[r+1][c] and A[r][c+1] and A[r+1][c+1]:
            answer += 1
print(answer)