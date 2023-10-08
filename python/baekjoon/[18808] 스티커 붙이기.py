# https://www.acmicpc.net/problem/18808
from sys import stdin
input = stdin.readline

def put(sticker):
    R, C = len(sticker), len(sticker[0])
    for r in range(N-R+1):
        for c in range(M-C+1):
            can = True
            for i in range(R):
                for j in range(C):
                    if matrix[r+i][c+j] & sticker[i][j]:
                        can = False
                        break
                if not can: break
            else:
                global answer
                for i in range(R):
                    for j in range(C):
                        if sticker[i][j]:
                            matrix[r+i][c+j] = 1
                            answer += 1
                return True

N, M, K = map(int, input().split())
matrix = [[0]*M for _ in range(N)]
answer = 0
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    if not put(sticker):
        sticker = list(zip(*sticker[::-1]))
        if not put(sticker):
            sticker = list(zip(*sticker[::-1]))
            if not put(sticker):
                sticker = list(zip(*sticker[::-1]))
                put(sticker)
print(answer)