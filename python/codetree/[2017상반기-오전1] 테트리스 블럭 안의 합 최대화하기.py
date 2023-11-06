import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tetris = [
    (0,0),(0,1),(0,2),(0,3),
    (1,0),(1,1),(1,2),
    (2,0),(2,1),
    (3,0)
]
# 0 1 2 3
# 4 5 6
# 7 8
# 9
tetro = [
    (0,1,2,3),(0,4,7,9),(0,1,4,5),
    (0,4,5,8),(1,4,5,7),(0,1,5,6),(1,2,4,5),
    (0,1,2,4),(0,1,2,6),(0,4,5,6),(2,4,5,6),(0,4,7,8),(1,5,7,8),(0,1,4,7),(0,1,5,8),
    (0,4,5,7),(0,1,2,5),(1,4,5,8),(1,4,5,6)
]
A = [list(map(int, input().split())) + [0]*3 for _ in range(N)]\
    + [[0]*(M+3) for _ in range(3)]
answer = 0
for r in range(N):
    for c in range(M):
        for tt in tetro:
            result = 0
            for t in tt:
                dx, dy = tetris[t]
                result += A[r+dx][c+dy]
            answer = max(result, answer)
print(answer)