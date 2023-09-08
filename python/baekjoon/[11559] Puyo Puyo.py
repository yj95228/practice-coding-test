# https://www.acmicpc.net/problem/11559
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(r,c):
    global puyopuyo
    queue = deque([(r,c)])
    color = matrix[r][c]
    visited = [[False]*12 for _ in range(6)]
    visited[r][c] = True

    # puyo : 같은 색 뿌요
    puyo = 1
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < 6 and 0 <= ny < 12 and\
            not visited[nx][ny] and matrix[nx][ny] == color:
                visited[nx][ny] = True
                puyo += 1
                queue.append((nx,ny))

    if puyo >= 4:
        # puyopuyo : 뿌요뿌요 완성
        puyopuyo = True
        for r in range(6):
            for c in range(12):
                if visited[r][c]:
                    matrix[r][c] = '.'

# 중력이 왼쪽으로 가는게 더 편해서 zip으로 변환해줌
matrix = [list(input().rstrip()) for _ in range(12)]
matrix = list(map(list, zip(*matrix[::-1])))

answer = 0
while True:
    puyopuyo = False
    for r in range(6):
        for c in range(12):
            if matrix[r][c] != '.':
                bfs(r,c)

    # 뿌요뿌요 완성되면 연쇄 += 1
    if puyopuyo: answer += 1
    else: break

    for r in range(6):
        # 문자열로 바꿔줘서 '.' 없애주고 없애준 만큼 뒤에 '.' 더해주기
        arr = list(''.join(''.join(matrix[r]).split('.')))
        arr += ['.']*(12-len(arr))
        matrix[r] = arr

print(answer)