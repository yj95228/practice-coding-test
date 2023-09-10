# [15686] 치킨 배달과 유사한 문제 (https://www.acmicpc.net/problem/15686)
# 1차 제출: 13/19 부분 성공 (119299kb, 4624ms)
# 2차 제출: 최솟값 갱신하고 break를 안 지웠음 (118188kb, 4660ms)
# 3차 제출: 시간 너무 긴 것 같아서 가지치기 (4660ms -> 4808ms)
# 4차 제출: 큐 안에서 말고 밖에서 가지치기 (4660ms -> 4708ms)
# 5차 제출: did6436 코드 참고 (180ms)
# https://www.acmicpc.net/problem/21278
import sys
from collections import deque
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 치킨 건물 2개, 모든 도시에서의 왕복 시간 합
chicken, answer = [0,0], 987654321
for i in range(1,N):
    for j in range(i+1,N+1):
        result = 0
        for k in range(1,N+1):
            if k == i or k == j: continue
            queue = deque([(0, k)])
            visited = [False]*(N+1)
            visited[k] = True
            while queue:
                distance, current = queue.popleft()
                if current == i or current == j:
                    result += distance
                    break
                for next in graph[current]:
                    if visited[next]: continue
                    visited[next] = True
                    queue.append((distance+2, next))
            if result > answer: break
        if result < answer:
            answer = result
            chicken = [i,j]
print(*chicken, answer)


# FIXME: 인접리스트말고 인접 행렬로 푸는 방식
N, M = map(int, input().split())
graph = [[99]*(N+1) for _ in range(N+1)]
for x in range(1,N+1):
    graph[x][x] = 0
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 2
    graph[B][A] = 2

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j: continue
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

answer = 987654321987
chicken = []
for i in range(1,N):
    for j in range(i+1,N+1):
        distance = 0
        for k in range(1,N+1):
            distance += min(graph[k][i], graph[k][j])
        if distance < answer:
            chicken = [i,j]
            answer = distance
print(*chicken, answer)