# https://www.acmicpc.net/problem/20327
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def flip1(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[i+2**l-r-1][j+c]
    return new_matrix

def flip2(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[i+r][j+2**l-c-1]
    return new_matrix

def rotate90(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[i+2**l-c-1][j+r]
    return new_matrix

def rotate_90(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[i+c][j+2**l-r-1]
    return new_matrix

def big_flip1(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[2**N-2**l-i+r][j+c]
    return new_matrix

def big_flip2(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[i+r][2**N-2**l-j+c]
    return new_matrix

def big_rotate90(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[2**N-2**l-j+r][i+c]
    return new_matrix

def big_rotate_90(l):
    new_matrix = [row[:] for row in matrix]
    for i in range(0,2**N,2**l):
        for j in range(0,2**N,2**l):
            for r in range(2**l):
                for c in range(2**l):
                    new_matrix[i+r][j+c] = matrix[j+r][2**N-2**l-i+c]
    return new_matrix

N, R = map(int, input().split())
matrix = [input().split() for _ in range(2**N)]
for _ in range(R):
    K, L = map(int, input().split())
    if K == 1:
        matrix = flip1(L)
    elif K == 2:
        matrix = flip2(L)
    elif K == 3:
        matrix = rotate90(L)
    elif K == 4:
        matrix = rotate_90(L)
    elif K == 5:
        matrix = big_flip1(L)
    elif K == 6:
        matrix = big_flip2(L)
    elif K == 7:
        matrix = big_rotate90(L)
    elif K == 8:
        matrix = big_rotate_90(L)
for row in matrix:
    print(*row)