# https://www.acmicpc.net/problem/5014
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
visited[S] = 1
queue = [S]
while queue:
    current = queue.pop(0)
    if current == G: break
    for dx in [U,-D]:
        if 1 <= current+dx <= F and not visited[current+dx]:
            visited[current+dx] = visited[current]+1
            queue.append(current+dx)
print(visited[G]-1 if visited[G] else 'use the stairs')