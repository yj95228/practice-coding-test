# FIXME: answer 초기값 잘 정해두기
# 1차 제출 : 정해진 모양이 정사각형이라 헷갈리긴 했지만 성공 (116160kb, 252ms)
# 2차 제출 : answer를 원래 matrix 중 최댓값으로 했는데 그냥 -1001로 설정 (252ms -> 276ms)
# https://www.acmicpc.net/problem/20002
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N = int(input())
matrix = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
answer = -1001
for r in range(1,N+1):
    for c in range(1,N+1):
        matrix[r][c] += matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1]
for i in range(N+1):
    for j in range(N+1):
        for k in range(1,N+1-max(i,j)):
            answer = max(answer, matrix[i+k][j+k]-matrix[i][j+k]-matrix[i+k][j]+matrix[i][j])
print(answer)