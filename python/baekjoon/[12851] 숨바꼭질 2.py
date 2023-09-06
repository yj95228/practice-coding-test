# 1차 제출 : 메모리 초과 (visited 배열 딕셔너리 사용)
# 2차 제출 : 틀렸습니다 (21라인 visited[current] < visited[current+x] 조건 없어서)
# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0
visited = [0]*200001
queue = deque([N])
visited[N] = 1
while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        if current == K:
            answer += 1
        else:
            for x in (-1,1,current):
                if 0 <= current+x <= 200000 and\
                (not visited[current+x] or visited[current] < visited[current+x]):
                    visited[current+x] = visited[current]+1
                    queue.append(current+x)
    if answer: break
print(visited[K]-1, answer, sep='\n')