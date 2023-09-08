# https://www.acmicpc.net/problem/1941
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(arr):
    visited = [[False]*5 for _ in range(5)]
    queue = deque([arr[0]])
    visited[arr[0][0]][arr[0][1]] = True
    together = 1
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and\
            not visited[nx][ny] and (nx,ny) in arr:
                visited[nx][ny] = True
                queue.append((nx,ny))
                together += 1
    return together

def dfs(arr):
    global answer
    if list(map(lambda x: matrix[x//5][x%5], arr)).count('Y') >= 4:
        return
    elif len(arr) == 7:
        if bfs(list(map(lambda x: (x//5, x%5), arr))) == 7:
            answer += 1
        return
    for x in range(25):
        if not arr or arr[-1] < x:
            dfs(arr+[x])

matrix = [list(input().rstrip()) for _ in range(5)]
answer = 0
dfs([])
print(answer)