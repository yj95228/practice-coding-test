# https://www.acmicpc.net/problem/30032
import sys
input = sys.stdin.readline

def change1(x):
    if x == 'd':
        return 'q'
    elif x == 'b':
        return 'p'
    elif x == 'q':
        return 'd'
    elif x == 'p':
        return 'b'

def change2(x):
    if x == 'd':
        return 'b'
    elif x == 'b':
        return 'd'
    elif x == 'q':
        return 'p'
    elif x == 'p':
        return 'q'

N, D = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]

if D == 1:
    for row in matrix:
        print(''.join(list(map(change1, row))))
else:
    for row in matrix:
        print(''.join(list(map(change2, row))))