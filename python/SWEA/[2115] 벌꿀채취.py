# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu
import sys
sys.stdin = open('input.txt', 'r')

def recur(r, c, n, result, square):
    global sm
    if n == M:
        sm = max(sm, square)
        return
    x = matrix[r][c+n]
    if result+x <= C:
        recur(r, c, n+1, result+x, square+x**2)
    recur(r, c, n+1, result, square)

T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for r1 in range(N):
        for c1 in range(N-M+1):
            sm = 0
            recur(r1,c1,0,0,0)
            sm1 = sm
            for r2 in range(N):
                for c2 in range(N-M+1):
                    if r1 == r2 and c2 <= c1+M: continue
                    sm = 0
                    sm2 = recur(r2,c2,0,0,0)
                    sm2 = sm
                    answer = max(answer, sm1+sm2)

    print(f'#{tc} {answer}')