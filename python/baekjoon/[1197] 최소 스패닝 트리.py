# TODO: 최소 스패닝 트리(MST)는 visited 배열 필요없음
# https://www.acmicpc.net/problem/1197
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def union(a,b):
    parents[find(b)] = find(a)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

V, E = map(int, input().split())
parents = [x for x in range(V+1)]
MST = []
for _ in range(E):
    A, B, C = map(int, input().split())
    MST.append((A,B,C))
MST.sort(key=lambda x: x[2])
answer, cnt = 0, 0
for a, b, c in MST:
    if cnt == V-1: break    # 종료 조건으로 시간 단축
    if find(a) != find(b):
        answer += c
        cnt += 1
        union(a,b)
print(answer)