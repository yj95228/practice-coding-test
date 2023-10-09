# https://www.acmicpc.net/problem/14890
from sys import stdin
input = stdin.readline

def check(row):
    road = [False]*N
    c = 1
    while c < N:
        height = row[c-1]

        if row[c] == height: c += 1
        elif row[c] > height+1 or row[c] < height-1: return 0

        # 올라가는 경사로
        elif row[c] == height+1:
            for i in range(1,L+1):
                if 0 <= c-i and row[c-i] == row[c]-1: continue
                else: return 0
            else:
                for i in range(1,L+1):
                    if not road[c-i]:
                        road[c-i] = True
                    else: return 0
                c += 1

        # 내려가는 경사로
        elif row[c] == height-1:
            for i in range(L):
                if c+i < N and row[c+i] == height-1: continue
                else: return 0
            else:
                for i in range(L):
                    if not road[c+i]:
                        road[c+i] = True
                    else: return 0
                c += L
    return 1

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for row in matrix:
    answer += check(row)
for row in zip(*matrix):
    answer += check(row)
print(answer)