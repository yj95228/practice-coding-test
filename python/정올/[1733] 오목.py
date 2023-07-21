# https://jungol.co.kr/problem/1733

import sys

sys.stdin=open("python\정올\input.txt","rt")
input = sys.stdin.readline

def check(row, col):
    global result
    dx, dy = [1, 0, 1, -1], [0, 1, 1, 1]
    row, col = row-1, col-1
    
    for i in range(4): # 방향
        result = False
        for j in range(1,5): #1,2,3,4칸
            if 0 <= row+j*dx[i] < 19 and 0 <= col+j*dy[i] < 19 \
            and matrix[row][col] == matrix[row+j*dx[i]][col+j*dy[i]]:
                result = True
            else:
                result = False
                break

        if 0 <= row+5*dx[i] < 19 and 0 <= col+5*dy[i] < 19 \
        and matrix[row][col] == matrix[row+5*dx[i]][col+5*dy[i]]:
            result = False
        if 0 <= row-dx[i] < 19 and 0 <= col-dy[i] < 19 \
        and matrix[row][col] == matrix[row-dx[i]][col-dy[i]]:
            result = False

        if result:
            return result
            
    return result

matrix = []
for _ in range(19):
    matrix.append(input().split())

win = False
for i in range(1,20):
    for j in range(1,20):
        if (matrix[i-1][j-1] == '1' or matrix[i-1][j-1] == '2') and check(i,j):
            win = True
            print(matrix[i-1][j-1])
            print(f'{i} {j}')
            break

if not win:
    print(0)