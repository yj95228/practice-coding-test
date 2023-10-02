# https://www.acmicpc.net/problem/14499
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def play():
    if matrix[r][c] == '0':
        matrix[r][c] = dice[0]
    else:
        dice[0] = matrix[r][c]
        matrix[r][c] = '0'
    print(dice[2], dice)

EAST, WEST, NORTH, SOUTH = '1','2','3','4'
N, M, r, c, K = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
# FIXME: 문자열로 통일 안한 실수
dice = ['0']*6      # 밑, 뒤, 윗, 앞, 동, 서
command = list(input().split())
for x in command:
    if x == EAST:
        if c < M-1:
            c += 1
            dice = [dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]]
            play()
    elif x == WEST:
        if c > 0:
            c -= 1
            dice = [dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]]
            play()
    elif x == NORTH:
        if r > 0:
            r -= 1
            dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
            play()
    elif x == SOUTH:
        if r < N-1:
            r += 1
            dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
            play()

# 2차 풀이
N, M, X, Y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(lambda x: int(x)-1, input().split()))
dice = [0]*6
dt = ((0,1),(0,-1),(-1,0),(1,0))
turn = [
    [3,1,0,5,4,2],
    [2,1,5,0,4,3],
    [4,0,2,3,5,1],
    [1,5,2,3,0,4]
]

for k in range(K):
    d = arr[k]
    dx, dy = dt[d]
    nx, ny = X+dx, Y+dy
    if 0 <= nx < N and 0 <= ny < M:
        dice = list(map(lambda x: dice[x], turn[d]))
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = dice[-1]
        else:
            matrix[nx][ny], dice[-1] = 0, matrix[nx][ny]
        print(dice[0])
        X, Y = nx, ny