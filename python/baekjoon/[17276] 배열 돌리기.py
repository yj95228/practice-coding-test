# FIXME: 90도, 180도 회전은 전체 배열 시계방향 회전이 아닌 문제에 명시된대로
# https://www.acmicpc.net/problem/17276
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def rotate45():
    new_matrix = [row[:] for row in matrix]
    for x in range(N):
        new_matrix[x][N//2] = matrix[x][x]
        new_matrix[x][N-x-1] = matrix[x][N//2]
        new_matrix[N//2][x] = matrix[N-x-1][x]
        new_matrix[x][x] = matrix[N//2][x]
    return new_matrix

def rotate_45():
    new_matrix = [row[:] for row in matrix]
    for x in range(N):
        new_matrix[N//2][x] = matrix[x][x]
        new_matrix[x][x] = matrix[x][N//2]
        new_matrix[x][N//2] = matrix[x][N-x-1]
        new_matrix[N-x-1][x] = matrix[N//2][x]
    return new_matrix

T = int(input())
for tc in range(1,T+1):
    N, D = map(int, input().split())
    matrix = [input().split() for _ in range(N)]
    if D == 45 or D == -315:
        matrix = rotate45()
    elif D == 90 or D == -270:
        matrix = rotate45()
        matrix = rotate45()
    elif D == 135 or D == -225:
        matrix = rotate45()
        matrix = rotate45()
        matrix = rotate45()
    elif D == 180 or D == -180:
        matrix = rotate45()
        matrix = rotate45()
        matrix = rotate45()
        matrix = rotate45()
    elif D == 225 or D == -135:
        matrix = rotate_45()
        matrix = rotate_45()
        matrix = rotate_45()
    elif D == 270 or D == -90:
        matrix = rotate_45()
        matrix = rotate_45()
    elif D == 315 or D == -45:
        matrix = rotate_45()
    for row in matrix:
        print(*row)