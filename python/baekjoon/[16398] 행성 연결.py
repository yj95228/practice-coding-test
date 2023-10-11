# https://www.acmicpc.net/problem/16398
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def prim(start):
    queue = [(0, start)]
    MST = [False]*N
    answer = 0

    while queue:
        weight, current = heappop(queue)
        if not MST[current]:
            MST[current] = True
            answer += weight
            for i, x in enumerate(matrix[current]):
                if current == i: continue
                elif not MST[i]:
                    heappush(queue, (x, i))
    return answer

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(prim(0))