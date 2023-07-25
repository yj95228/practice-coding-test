# https://www.acmicpc.net/problem/18111

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline

N, M, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

mintime = float('inf')
answer = 0
for num in range(257):
    time = 0
    inv = B
    for i in range(N):
        for j in range(M):
            tmp = num - matrix[i][j]
            if tmp >= 0:
                time += tmp
                inv -= tmp
            else:
                time -= 2*tmp
                inv -= tmp
    if time <= mintime and inv >= 0:
        mintime = time
        answer = num
print(mintime, answer)