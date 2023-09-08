# TODO: DFS 변수를 어떻게 설정할지 어려웠음
# FIXME: 변수에 A그룹, B그룹에 각각 더하는 방식 해도 됐을듯
# 연결되어있는지 dfs로 확인해도 괜찮을 것 같음
# https://www.acmicpc.net/problem/17471
import sys
from collections import deque
input = sys.stdin.readline

def connected(arr):
    if not arr: return False
    queue = deque([arr[0]])
    visited = [False]*(N+1)
    visited[arr[0]] = True
    cnt = 1
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if next in arr and not visited[next]:
                visited[next] = True
                cnt += 1
                queue.append(next)
    return len(arr) == cnt


def dfs(selected, unselected):
    global answer
    if connected(selected) and connected(unselected):
        result = sum(map(lambda x: people[x], selected))
        answer = min(answer, abs(result-(sm-result)))
    for x in range(1,N+1):
        if not selected or selected[-1] < x:
            if x in unselected:
                unselected.remove(x)
                dfs(selected+[x], unselected)
                unselected.append(x)

N = int(input())
people = [0] + list(map(int, input().split()))
graph = [set() for _ in range(N+1)]
for i in range(N):
    connect, *lst = map(int, input().split())
    for x in lst:
        graph[i+1].add(x)
        graph[x].add(i+1)
sm = sum(people)
answer = sm
dfs([], [x+1 for x in range(N)])
print(-1 if answer == sm else answer)