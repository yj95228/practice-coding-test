# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
import sys
sys.stdin = open('input.txt', 'r')

def recur(n, alst, a, blst, b):
    global answer
    if n == N:
        if len(alst) == len(blst):
            answer = min(abs(a-b), answer)
        return

    if abs(len(alst)-len(blst))-(N-n) > 0: return

    recur(n+1, alst+[n], a+sum([matrix[n][x] for x in alst] + [matrix[x][n] for x in alst]), blst, b)
    recur(n+1, alst, a, blst+[n], b+sum([matrix[n][x] for x in blst] + [matrix[x][n] for x in blst]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 987654321
    recur(0, [], 0, [], 0)
    print(f'#{tc} {answer}')