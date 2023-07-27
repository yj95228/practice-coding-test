# https://www.acmicpc.net/problem/2578
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
matrix = [list(map(int, input().split())) for _ in range(5)]
num = [x for _ in range(5) for x in list(map(int, input().split()))]
bingo = [0]*12
for i, x in enumerate(num):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == x:
                matrix[r][c] = 0
                if sum(matrix[r]) == 0:
                    bingo[r] = 1
                if sum([row[c] for row in matrix]) == 0:
                    bingo[5+c] = 1
                if r == c and (matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3]+matrix[4][4]) == 0:
                    bingo[10] = 1
                if r == 4-c and (matrix[0][4]+matrix[1][3]+matrix[2][2]+matrix[3][1]+matrix[4][0]) == 0:
                    bingo[11] = 1
                if sum(bingo) >= 3:
                    print(i+1)
                    break
        if sum(bingo) >= 3: break
    if sum(bingo) >= 3: break