import sys
input = sys.stdin.readline

def rotate(A, x):
    B = [[0]*NN for _ in range(NN)]
    MM = 2**x
    for i in range(0, NN, MM):
        for j in range(0, NN, MM):
            for k in range(0, MM, MM//2):
                for l in range(0, MM, MM//2):
                    for r in range(MM//2):
                        for c in range(MM//2):
                            B[i+l+r][j+MM-k-MM//2+c] = A[i+k+r][j+l+c]
    return B

N, Q = map(int, input().split())
NN = 2**N
A = [list(map(int, input().split())) for _ in range(NN)]
arr = list(map(int, input().split()))
for x in arr:
    if x: A = rotate(A, x)
    B = [row[:] for row in A]
    for r in range(NN):
        for c in range(NN):
            if not A[r][c]: continue
            cnt = 4
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < NN and 0 <= ny < NN and A[nx][ny]: continue
                cnt -= 1
                if cnt <= 2:
                    B[r][c] -= 1
                    break
    A = B
answer, mx = 0, 0
V = [[0]*NN for _ in range(NN)]
for r in range(NN):
    for c in range(NN):
        if not V[r][c] and A[r][c]:
            V[r][c] = 1
            cnt = 1
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                answer += A[x][y]
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < NN and 0 <= ny < NN and not V[nx][ny] and A[nx][ny]:
                        V[nx][ny] = 1
                        cnt += 1
                        stack.append((nx, ny))
            mx = max(mx, cnt)
print(answer)
print(mx)