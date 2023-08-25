# https://www.acmicpc.net/problem/16235
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def spring(r,c):
    alive, die = [], 0
    for tree in sorted(trees[r][c]):
        if tree <= yangboon[r][c]:
            yangboon[r][c] -= tree
            alive.append(tree+1)
        else: die += tree//2
    trees[r][c] = alive
    summer[r][c] = die

def fall(r,c):
    for tree in trees[r][c]:
        if tree%5 == 0:
            for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                if 0 <= r+dx < N and 0 <= c+dy < N:
                    trees[r+dx][c+dy].append(1)


N, M, K = map(int, input().split())
winter = [list(map(int, input().split())) for _ in range(N)]
yangboon = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for year in range(K):
    summer = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if trees[r][c]: spring(r,c)

    for r in range(N):
        for c in range(N):
            yangboon[r][c] += summer[r][c]

    for r in range(N):
        for c in range(N):
            if trees[r][c]: fall(r,c)

    for r in range(N):
        for c in range(N):
            yangboon[r][c] += winter[r][c]

print(sum(map(len, sum(trees,[]))))