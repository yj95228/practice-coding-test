# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1,TC+1):
    N, M, K, T = map(int, input().split())
    matrix = [[set() for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        t, si, sj, h, w = map(int, input().split())
        for i in range(si, min(N,si+h)):
            for j in range(sj, min(M,sj+w)):
                matrix[i][j].add(t)
    answer = 0
    for r in range(N):
        for c in range(M):
            if len(matrix[r][c]) != T+1: answer += 1
    print(f'#{tc} {answer}')