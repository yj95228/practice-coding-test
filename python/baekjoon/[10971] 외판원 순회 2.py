'''
- 1차 시도: 35% 틀렸습니다 - 도시 i에서 j로 갈 수 없는 경우를 처리 하지 않음
- 2차 시도: 35% 틀렸습니다 - 마지막 처음 도시로 돌아갈 때 갈 수 없는 경우를 처리 하지 않음
- 3차 시도: 117968kb, 1080ms
- 4차 시도: 115960kb, 180ms - 이미 answer보다 크면 가지치기
'''
# https://www.acmicpc.net/problem/10971https://www.acmicpc.net/problem/10971
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def recur(n, start, x, result):
    global answer
    if answer < result: return
    if n == N-1:
        if matrix[x][start]:
            answer = min(answer, result+matrix[x][start])
        return
    for i in range(N):
        if i == x or i == start: continue
        elif not visited[i] and matrix[x][i]:
            visited[i] = True
            recur(n+1, start, i, result+matrix[x][i])
            visited[i] = False

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321
for x in range(N):
    visited = [False]*N
    recur(0, x, x, 0)
print(answer)