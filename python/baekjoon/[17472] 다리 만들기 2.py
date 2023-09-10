# 1차 제출: N, M 확인 안해서 고침 (x3번 실수)
# 2차 제출: 혹시 MST 안에 값들이 중복이어서 그런건지 확인하기 위해 list(set(MST))로 변환 (sort 때문에 다시 list로)
# 3차 제출: 양뱡향으로 연결되어 있지 않아서 그런건지 확인해보기
# 4차 제출: 간선을 cnt개수만큼만 넣도록 (x2)
# 5차 제출: len(set(parents))말고 간선 수만큼만 더했어야 했음 (113112kb, 112ms)
# 최소 스패닝 트리 문제인 것 같은데 전에 배운 코드 복붙해옴.. 외우자...
# https://www.acmicpc.net/problem/17472
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 2
# 섬 번호 만들기
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            stack = [(r,c)]
            matrix[r][c] = cnt
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= x+dx < N and 0 <= y+dy < M and matrix[nx][ny] == 1:
                        matrix[nx][ny] = cnt
                        stack.append((nx,ny))
            cnt += 1

# 섬 간의 거리 찾기
graph = [set() for _ in range(cnt-1)]
MST = []
dt = [(1,0),(0,1),(-1,0),(0,-1)]
for r in range(N):
    for c in range(M):
        if matrix[r][c]:
            for i in range(4):
                dx, dy = dt[i]
                go = 1
                while True:
                    nx, ny = r+go*dx, c+go*dy
                    if not (0 <= nx < N and 0 <= ny < M): break
                    elif matrix[nx][ny] == 0: go += 1
                    elif matrix[nx][ny] != matrix[r][c] and go > 2:
                        MST.append((matrix[r][c]-1, matrix[nx][ny]-1, go-1))
                        break
                    else: break
                        
def union(a,b):
    parents[find(b)] = find(a)

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

parents = [x for x in range(cnt-1)]
MST = sorted(list(set(MST)), key=lambda x: x[2])
answer = 0
for a, b, c in MST:
    if cnt == 3:
        print(answer)
        break
    if find(a) != find(b):
        union(a,b)
        answer += c
        cnt -= 1
else: print(-1)