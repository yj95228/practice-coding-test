# 1차 제출: (65분 소요) 136196kb, 3056ms
# 2차 제출: 회전을 zip말고 for문으로 순회 (3056ms -> 592ms)
# 3차 제출: 얼음이 남아있는 것만 녹일지 확인 (592ms -> 668ms)
# 4차 제출: deque BFS -> stack DFS (592ms -> 616ms)
# https://www.acmicpc.net/problem/1913
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def magic(n):
    # 마법 시전
    new = [[0]*length for _ in range(length)]
    for i in range(2**(N-n)):
        for j in range(2**(N-n)):
            for r in range(2**n):
                for c in range(2**n):
                    new[2**n*i+r][2**n*j+c] = matrix[2**n*i+(2**n-c)-1][2**n*j+r]
    # 얼음 녹이기
    melt = []
    for r in range(length):
        for c in range(length):
            ice = 0
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < length and 0 <= ny < length and new[nx][ny]:
                    ice += 1
            if ice < 3: melt.append((r,c))
    for r, c in melt: new[r][c] = max(new[r][c]-1, 0)
    return new

N, Q = map(int, input().split())
length = 2**N
matrix = [list(map(int, input().split())) for _ in range(length)]
L = list(map(int, input().split()))
for l in L:
    matrix = magic(l)

# BFS
answer, cnt = 0, 0
visited = [[False]*length for _ in range(length)]
for r in range(length):
    for c in range(length):
        if matrix[r][c]:
            answer += matrix[r][c]
            if not visited[r][c]:
                visited[r][c] = True
                queue = deque([(r,c)])
                result = 1
                while queue:
                    x, y = queue.popleft()
                    cnt = max(result, cnt)
                    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < length and 0 <= ny < length and\
                        not visited[nx][ny] and matrix[nx][ny]:
                            visited[nx][ny] = True
                            result += 1
                            queue.append((nx,ny))
print(answer)
print(cnt)