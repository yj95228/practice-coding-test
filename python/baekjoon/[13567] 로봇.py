<<<<<<< HEAD
=======
# TODO : 다시 풀어보기
>>>>>>> 07f2565049530a9c86644c7cab0248236ce8d070
# https://www.acmicpc.net/problem/13567
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [[0]*(M+1) for _ in range(M+1)]
r,c = 0,0
matrix[r][c] = 'v'
turn_left = {'v':'>','>':'^','^':'<','<':'v'}
turn_right = {'v':'<','<':'^','^':'>','>':'v'}

for _ in range(N):
    comm, d = input().split()
    d = int(d)
    direction = matrix[r][c]
    if comm == 'TURN' and d == 0:
        matrix[r][c] = turn_left[direction]
    elif comm == 'TURN' and d == 1:
        matrix[r][c] = turn_right[direction]
    else:
        if direction == 'v' and 0 <= r+d < M+1:
            matrix[r][c] = 0
            r += d
            matrix[r][c] = direction
        elif direction == '>' and 0 <= c+d < M+1:
            matrix[r][c] = 0
            c += d
            matrix[r][c] = direction
        elif direction == '^' and 0 <= r-d < M+1:
            matrix[r][c] = 0
            r -= d
            matrix[r][c] = direction
        elif direction == '<' and 0 <= c-d < M+1:
            matrix[r][c] = 0
            c -= d
            matrix[r][c] = direction
        else:
            print(-1)
            break
else:
    print(f'{r} {c}')