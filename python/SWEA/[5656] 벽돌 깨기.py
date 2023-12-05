# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
import sys
sys.stdin = open('input.txt', 'r')

def down(arr):
    for c in range(W):
        for r in range(H-1,-1,-1):
            if arr[r][c] == 0:
                now = r
                while 0 < now and arr[now][c] == 0: now -= 1
                arr[now][c], arr[r][c] = arr[r][c], arr[now][c]
    return arr

def side_effect(arr,r,c,x):
    if x == 0: return arr
    else:
        arr[r][c] = 0
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            for i in range(1,x):
                nx, ny = r+i*dx, c+i*dy
                if 0 <= nx < H and 0 <= ny < W:
                    y = arr[nx][ny]
                    arr = side_effect(arr,nx,ny,y)
                else: break
    return arr

def play(arr, c):
    for r in range(H):
        x = arr[r][c]
        if not x: continue
        arr[r][c] = 0
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            for i in range(x):
                nx, ny = r+i*dx, c+i*dy
                if 0 <= nx < H and 0 <= ny < W:
                    y = arr[nx][ny]
                    if y > 1:
                        arr = side_effect(arr,nx,ny,y)
                    arr[nx][ny] = 0
                else: break
        break
    return down(arr)

def recur(n, arr):
    global answer
    if n == N:
        sm = 0
        for r in range(H):
            for c in range(W):
                if arr[r][c]:
                    sm += 1
        answer = min(answer, sm)
        return
    for i in range(W):
        recur(n+1, play([row[:] for row in arr], i))

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    answer = 987654321
    recur(0, matrix)
    print(f'#{tc} {answer}')

# 2차 풀이
from itertools import product


def play(A, pp):
    B = [row[:] for row in A]
    for p in pp:
        rr = -1
        for r in range(H):
            if B[r][p]:
                rr = r;
                break
        if rr == -1: continue

        queue = [(B[rr][p], rr, p)]
        while queue:
            next_q = []
            for num, r, c in queue:
                B[r][c] = 0
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    for k in range(1, num):
                        nx, ny = r + k * dx, c + k * dy
                        if 0 <= nx < H and 0 <= ny < W:
                            if B[nx][ny]:
                                next_q.append((B[nx][ny], nx, ny))
            queue = next_q

        C = [[0] * W for _ in range(H)]
        for c in range(W):
            now = H - 1
            for r in range(H - 1, -1, -1):
                if B[r][c]:
                    C[now][c] = B[r][c]
                    now -= 1
        B = C
    return len([x for row in B for x in row if x])


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    answer = 987654321
    for p in product(range(W), repeat=N):
        answer = min(answer, play(A, p))
        if not answer: break
    print(f'#{tc} {answer}')
