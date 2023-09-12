# https://www.acmicpc.net/problem/16935
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def flip1():
    N = len(matrix)
    new_matrix = [row[:] for row in matrix]
    for r in range(N):
        new_matrix[N-r-1] = matrix[r]
    return new_matrix

def flip2():
    N, M = len(matrix), len(matrix[0])
    new_matrix = [row[:] for row in matrix]
    for r in range(N):
        for c in range(M):
            new_matrix[r][M-c-1] = matrix[r][c]
    return new_matrix

def rotate90():
    N, M = len(matrix), len(matrix[0])
    new_matrix = [[0]*N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            new_matrix[c][r] = matrix[N-1-r][c]
    return new_matrix

def rotate_90():
    N, M = len(matrix), len(matrix[0])
    new_matrix = [[0]*N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            new_matrix[c][r] = matrix[r][M-1-c]
    return new_matrix

def big_rotate90():
    N, M = len(matrix), len(matrix[0])
    new_matrix = [row[:] for row in matrix]
    for r in range(N//2):
        for c in range(M//2):
            new_matrix[r][M//2+c] = matrix[r][c]
            new_matrix[N//2+r][M//2+c] = matrix[r][M//2+c]
            new_matrix[N//2+r][c] = matrix[N//2+r][M//2+c]
            new_matrix[r][c] = matrix[N//2+r][c]
    return new_matrix

def big_rotate_90():
    N, M = len(matrix), len(matrix[0])
    new_matrix = [row[:] for row in matrix]
    for r in range(N//2):
        for c in range(M//2):
            new_matrix[N//2+r][+c] = matrix[r][c]
            new_matrix[r][c] = matrix[r][M//2+c]
            new_matrix[r][M//2+c] = matrix[N//2+r][M//2+c]
            new_matrix[N//2+r][M//2+c] = matrix[N//2+r][c]
    return new_matrix

N, M, R = map(int, input().split())
matrix = [input().split() for _ in range(N)]
arr = input().split()
for x in arr:
    if x == '1':
        matrix = flip1()
    elif x == '2':
        matrix = flip2()
    elif x == '3':
        matrix = rotate90()
    elif x == '4':
        matrix = rotate_90()
    elif x == '5':
        matrix = big_rotate90()
    elif x == '6':
        matrix = big_rotate_90()
for row in matrix:
    print(*row)