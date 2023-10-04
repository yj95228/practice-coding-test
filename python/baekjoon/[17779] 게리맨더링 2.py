'''
- 1차. 풀이시간 85분 -> 시간 초과
- 처음에 좌표 범위로 경계를 나누려다가 빡세서 dfs로 변경
- 2차. 풀이시간 115분 - 그냥 좌표로 풀기 (121388kb, 808ms)
- 3차. 1,2,3,4 선거구도 dfs말고 좌표 범위로 찾기 (808ms -> ?)
'''
# https://www.acmicpc.net/problem/17779
from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321
total = sum([x for row in matrix for x in row])
for x in range(N-2):
    for y in range(1,N-1):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if 0 <= x < x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:
                    result = [0]*5
                    square = [[0]*N for _ in range(N)]

                    for i in range(d1+1):
                        square[x+i][y-i] = 5
                        square[x+d2+i][y+d2-i] = 5
                    for i in range(d2+1):
                        square[x+i][y+i] = 5
                        square[x+d1+i][y-d1+i] = 5

                    for r in range(x+d1):
                        for c in range(y+1):
                            if square[r][c] == 5: break
                            result[0] += matrix[r][c]
                    for c in range(y+1,N):
                        for r in range(x+d2+1):
                            if square[r][c] == 5: break
                            result[1] += matrix[r][c]
                    for r in range(x+d1,N):
                        for c in range(y-d1+d2):
                            if square[r][c] == 5: break
                            result[2] += matrix[r][c]
                    for c in range(N-1,y-d1+d2-1,-1):
                        for r in range(N-1,x+d2,-1):
                            if square[r][c] == 5: break
                            result[3] += matrix[r][c]

                    result[4] = total-sum(result[:4])
                    answer = min(answer, max(result)-min(result))

print(answer)