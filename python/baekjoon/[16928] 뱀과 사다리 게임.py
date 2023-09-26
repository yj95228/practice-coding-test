# https://www.acmicpc.net/problem/16928
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def recur(now):
    global answer

    if now == 100:
        answer = min(answer, visited[now])
        return

    for x in range(6,0,-1):
        if now+x > 100: continue
        next = ls[now+x]
        if visited[now]+1 < visited[next]:
            visited[next] = visited[now]+1
            recur(next)

N, M = map(int, input().split())
ls = [x for x in range(101)]
for _ in range(N+M):
    u, v = map(int, input().split())
    ls[u] = v
visited = [100]*101
visited[1] = 0
answer = 100
recur(1)
print(answer)