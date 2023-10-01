'''
- 1차 제출: 15% 시간 초과
- 2차 제출: 19% 시간 초과 (첫방문 처리 + dfs 안에 arr 넘기는 대신 룩업테이블 + 26이면 빨리 return)
- 3차 제출: 틀렸습니다 (재귀 복귀 안 시킴)
- 4차 제출: 68% 시간 초과 (배열 위치 visited는 필요없음)
- 5차 제출: 195192kb, 6020ms (alphabet을 재귀 인자로 넘기지 않고 global 변수로 빼기)
'''
# https://www.acmicpc.net/problem/1987
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def recur(r,c,result):
    global answer, visited
    answer = max(answer, result)
    if answer == 26: return
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < R and 0 <= ny < C:
            alphabet = ord(matrix[nx][ny])-ord('A')
            if not visited[alphabet]:
                visited[alphabet] = True
                recur(nx,ny,result+1)
                visited[alphabet] = False

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
visited = [False]*26
visited[ord(matrix[0][0])-ord('A')] = True
answer = 0
recur(0,0,1)
print(answer)