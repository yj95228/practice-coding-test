# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([N])
visited = [0]*200001
visited[N] = 1
while queue:
    v = queue.popleft()
    if v == K:
        print(visited[v]-1)
        break
    # visit한 경우와 하지 않은 경우 따로 처리
    if v//2 <= K+1 and 0 < v <= 100000 and\
    (not visited[2*v] or visited[v] < visited[2*v]):
        visited[2*v] = visited[v]
        queue.insert(0,2*v)
    if v <= 100000 and not visited[v+1]:
        visited[v+1] = visited[v]+1
        queue.append(v+1)
    if 0 < v and not visited[v-1]:
        visited[v-1] = visited[v]+1
        queue.append(v-1)